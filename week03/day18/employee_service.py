import sqlite3

try:
    from .database import get_connection
except ImportError:  # pragma: no cover - allows direct execution
    from database import get_connection


def create_employee(name, department, salary, email):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO employees (name, department, salary, email)
            VALUES (?, ?, ?, ?)
            """,
            (name, department, salary, email),
        )
        connection.commit()
        employee_id = cursor.lastrowid
        return employee_id
    except sqlite3.IntegrityError as exc:
        connection.rollback()
        raise ValueError("Employee already exists") from exc
    finally:
        connection.close()


def get_employees():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, department, salary, email FROM employees ORDER BY id")
    rows = cursor.fetchall()
    connection.close()

    return [
        {"id": row["id"], "name": row["name"], "department": row["department"], "salary": row["salary"], "email": row["email"]}
        for row in rows
    ]


def get_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, name, department, salary, email FROM employees WHERE id = ?",
        (employee_id,),
    )
    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return {"id": row["id"], "name": row["name"], "department": row["department"], "salary": row["salary"], "email": row["email"]}


def update_employee(employee_id, name=None, department=None, salary=None, email=None):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        if name is not None:
            cursor.execute("UPDATE employees SET name = ? WHERE id = ?", (name, employee_id))
        if department is not None:
            cursor.execute("UPDATE employees SET department = ? WHERE id = ?", (department, employee_id))
        if salary is not None:
            cursor.execute("UPDATE employees SET salary = ? WHERE id = ?", (salary, employee_id))
        if email is not None:
            cursor.execute("UPDATE employees SET email = ? WHERE id = ?", (email, employee_id))

        connection.commit()
        return get_employee(employee_id)
    except sqlite3.IntegrityError as exc:
        connection.rollback()
        raise ValueError("Employee already exists") from exc
    finally:
        connection.close()


def delete_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
        connection.commit()
        return cursor.rowcount > 0
    finally:
        connection.close()
