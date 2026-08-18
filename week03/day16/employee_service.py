
try:
    from .database import get_connection
except ImportError:  # pragma: no cover - allows direct import in simple runs
    from database import get_connection


def create_employee(name, department, salary):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO employees (name, department, salary)
        VALUES (?, ?, ?)
        """,
        (name, department, salary),
    )
    connection.commit()
    employee_id = cursor.lastrowid
    connection.close()
    return employee_id


def get_employees(department=None, min_salary=None):
    query = "SELECT id, name, department, salary FROM employees"
    params = []
    filters = []

    if department:
        filters.append("department = ?")
        params.append(department)

    if min_salary is not None:
        filters.append("salary >= ?")
        params.append(min_salary)

    if filters:
        query += " WHERE " + " AND ".join(filters)

    query += " ORDER BY id"

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    connection.close()

    return [
        {"id": row["id"], "name": row["name"], "department": row["department"], "salary": row["salary"]}
        for row in rows
    ]


def get_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, name, department, salary FROM employees WHERE id = ?",
        (employee_id,),
    )
    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return {"id": row["id"], "name": row["name"], "department": row["department"], "salary": row["salary"]}


def update_employee(employee_id, name=None, department=None, salary=None):
    connection = get_connection()
    cursor = connection.cursor()

    if name is not None:
        cursor.execute("UPDATE employees SET name = ? WHERE id = ?", (name, employee_id))
    if department is not None:
        cursor.execute("UPDATE employees SET department = ? WHERE id = ?", (department, employee_id))
    if salary is not None:
        cursor.execute("UPDATE employees SET salary = ? WHERE id = ?", (salary, employee_id))

    connection.commit()
    connection.close()
    return get_employee(employee_id)


def delete_employee(employee_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    connection.commit()
    connection.close()
    return cursor.rowcount > 0
