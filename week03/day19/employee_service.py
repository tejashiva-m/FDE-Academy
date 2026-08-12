from __future__ import annotations
import sqlite3

from schemas import EmployeeCreate, EmployeeUpdate


def create_employee(
    connection: sqlite3.Connection, employee: EmployeeCreate
) -> dict:
    cursor = connection.execute(
        """
        INSERT INTO employees (name, email, department, salary)
        VALUES (?, ?, ?, ?)
        """,
        (employee.name, employee.email, employee.department, employee.salary),
    )
    connection.commit()
    return get_employee(connection, cursor.lastrowid)


def list_employees(connection: sqlite3.Connection) -> list[dict]:
    rows = connection.execute("SELECT * FROM employees ORDER BY id").fetchall()
    return [dict(row) for row in rows]


def get_employee(
    connection: sqlite3.Connection, employee_id: int
) -> dict | None:
    row = connection.execute(
        "SELECT * FROM employees WHERE id = ?", (employee_id,)
    ).fetchone()
    return dict(row) if row else None


def update_employee(
    connection: sqlite3.Connection,
    employee_id: int,
    employee: EmployeeUpdate,
) -> dict | None:
    cursor = connection.execute(
        """
        UPDATE employees
        SET name = ?, email = ?, department = ?, salary = ?
        WHERE id = ?
        """,
        (
            employee.name,
            employee.email,
            employee.department,
            employee.salary,
            employee_id,
        ),
    )
    connection.commit()
    if cursor.rowcount == 0:
        return None
    return get_employee(connection, employee_id)


def delete_employee(connection: sqlite3.Connection, employee_id: int) -> bool:
    cursor = connection.execute(
        "DELETE FROM employees WHERE id = ?", (employee_id,)
    )
    connection.commit()
    return cursor.rowcount > 0
