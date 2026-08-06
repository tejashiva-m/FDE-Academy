import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

cursor.execute(
    """
    DELETE FROM employees
    WHERE name = ?
    """,
    ("Teja",)
)

connection.commit()

print("Employee deleted.")

connection.close()

