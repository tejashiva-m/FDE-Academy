import sqlite3

connection = sqlite3.connect("company.db")

print("Database created successfully.")

connection.close()
