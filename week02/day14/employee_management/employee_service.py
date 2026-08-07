import csv
import json
import sqlite3
from pathlib import Path

try:
    from .database import get_connection, initialize_database
    from .employee import Employee
    from .logger import logger
except ImportError:  # pragma: no cover - allows direct execution
    from database import get_connection, initialize_database
    from employee import Employee
    from logger import logger


initialize_database()


def add_employee(name, department, salary):
    if not name or not str(name).strip():
        raise ValueError("Name cannot be empty")
    if salary < 0:
        raise ValueError("Salary cannot be negative")

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO employees (name, department, salary)
            VALUES (?, ?, ?)
            """,
            (str(name).strip(), str(department).strip(), salary),
        )
        connection.commit()
        employee_id = cursor.lastrowid
        connection.close()
        logger.info("Created employee %s", str(name).strip())
        return employee_id
    except sqlite3.Error as exc:
        logger.exception("Database error while creating employee")
        raise RuntimeError(f"Database error: {exc}") from exc


def get_all_employees():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT id, name, department, salary
            FROM employees
            ORDER BY id
            """
        )
        rows = cursor.fetchall()
        connection.close()
    except sqlite3.Error as exc:
        logger.exception("Database error while fetching employees")
        raise RuntimeError(f"Database error: {exc}") from exc

    return [Employee(id=row[0], name=row[1], department=row[2], salary=row[3]) for row in rows]


def search_employee(keyword):
    if not keyword or not str(keyword).strip():
        return []

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT id, name, department, salary
            FROM employees
            WHERE name LIKE ? OR department LIKE ?
            ORDER BY id
            """,
            (f"%{str(keyword).strip()}%", f"%{str(keyword).strip()}%"),
        )
        rows = cursor.fetchall()
        connection.close()
    except sqlite3.Error as exc:
        logger.exception("Database error while searching employees")
        raise RuntimeError(f"Database error: {exc}") from exc

    return [Employee(id=row[0], name=row[1], department=row[2], salary=row[3]) for row in rows]


def update_salary(employee_id, new_salary):
    if new_salary < 0:
        raise ValueError("Salary cannot be negative")

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            UPDATE employees
            SET salary = ?
            WHERE id = ?
            """,
            (new_salary, employee_id),
        )
        connection.commit()
        connection.close()
        logger.info("Updated salary for employee %s", employee_id)
        return cursor.rowcount > 0
    except sqlite3.Error as exc:
        logger.exception("Database error while updating salary")
        raise RuntimeError(f"Database error: {exc}") from exc


def delete_employee(employee_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            DELETE FROM employees
            WHERE id = ?
            """,
            (employee_id,),
        )
        connection.commit()
        connection.close()
        logger.info("Deleted employee %s", employee_id)
        return cursor.rowcount > 0
    except sqlite3.Error as exc:
        logger.exception("Database error while deleting employee")
        raise RuntimeError(f"Database error: {exc}") from exc


def get_average_salary():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT AVG(salary) AS average_salary FROM employees")
        result = cursor.fetchone()[0]
        connection.close()
        return round(float(result), 2) if result is not None else 0.0
    except sqlite3.Error as exc:
        logger.exception("Database error while computing average salary")
        raise RuntimeError(f"Database error: {exc}") from exc


def get_highest_salary():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(salary) AS highest_salary FROM employees")
        result = cursor.fetchone()[0]
        connection.close()
        return int(result) if result is not None else 0
    except sqlite3.Error as exc:
        logger.exception("Database error while computing highest salary")
        raise RuntimeError(f"Database error: {exc}") from exc


def get_lowest_salary():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT MIN(salary) AS lowest_salary FROM employees")
        result = cursor.fetchone()[0]
        connection.close()
        return int(result) if result is not None else 0
    except sqlite3.Error as exc:
        logger.exception("Database error while computing lowest salary")
        raise RuntimeError(f"Database error: {exc}") from exc


def get_employee_count():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) AS employee_count FROM employees")
        result = cursor.fetchone()[0]
        connection.close()
        return int(result) if result is not None else 0
    except sqlite3.Error as exc:
        logger.exception("Database error while counting employees")
        raise RuntimeError(f"Database error: {exc}") from exc


def get_department_breakdown():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT department, COUNT(*) AS employee_count
            FROM employees
            GROUP BY department
            ORDER BY department
            """
        )
        rows = cursor.fetchall()
        connection.close()
        return rows
    except sqlite3.Error as exc:
        logger.exception("Database error while computing department counts")
        raise RuntimeError(f"Database error: {exc}") from exc


def get_department_count():
    return len(get_department_breakdown())


def export_employees(path=None):
    employees = get_all_employees()
    export_path = Path(path) if path else Path(__file__).resolve().parent / "employees.json"

    payload = [
        {
            "id": employee.id,
            "name": employee.name,
            "department": employee.department,
            "salary": employee.salary,
        }
        for employee in employees
    ]

    with export_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)

    csv_path = export_path.with_suffix(".csv")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "name", "department", "salary"])
        writer.writeheader()
        for entry in payload:
            writer.writerow(entry)

    return export_path, csv_path