import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

name = input("Employee Name: ")

cursor.execute(
    """
    SELECT *
    FROM employees
    WHERE name = ?
    """,
    (name,)
)

employee = cursor.fetchone()

print(employee)

connection.close()