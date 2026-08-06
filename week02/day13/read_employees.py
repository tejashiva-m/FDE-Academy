import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

cursor.execute(
    "SELECT * FROM employees"
)

employees = cursor.fetchall()

for employee in employees:
    print(employee)

connection.close()

