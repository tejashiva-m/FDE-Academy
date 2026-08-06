import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

cursor.execute(
    """
    UPDATE employees
    SET salary = ?
    WHERE name = ?
    """,
    (150000, "Teja")
)

connection.commit()

print("Salary updated.")

connection.close()

