import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

cursor.execute(
    """
    INSERT INTO employees(name, department, salary)
    VALUES (?, ?, ?)
    """,
    ("Teja", "Cloud", 120000)
)

connection.commit()
connection.close()

print("Employee inserted.")