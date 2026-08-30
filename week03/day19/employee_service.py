from __future__ import annotations

from schemas import EmployeeCreate, EmployeeUpdate


def create_employee(connection, employee: EmployeeCreate) -> dict:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO employees (name, email, department, salary)
            VALUES (%s, %s, %s, %s)
            RETURNING id, name, email, department, salary
            """,
            (employee.name, employee.email, employee.department, employee.salary),
        )
        result = cursor.fetchone()
    connection.commit()
    return result


def list_employees(connection) -> list[dict]:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM employees ORDER BY id")
        return cursor.fetchall()


def get_employee(connection, employee_id: int) -> dict | None:
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM employees WHERE id = %s", (employee_id,))
        return cursor.fetchone()


def update_employee(
    connection,
    employee_id: int,
    employee: EmployeeUpdate,
) -> dict | None:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE employees
            SET name = %s, email = %s, department = %s, salary = %s
            WHERE id = %s
            """,
            (
                employee.name,
                employee.email,
                employee.department,
                employee.salary,
                employee_id,
            ),
        )
        updated = cursor.rowcount > 0
    connection.commit()
    if not updated:
        return None
    return get_employee(connection, employee_id)


def delete_employee(connection, employee_id: int) -> bool:
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
        deleted = cursor.rowcount > 0
    connection.commit()
    return deleted
