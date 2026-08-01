from pathlib import Path

file_path = Path(__file__).resolve().parent / "employees.txt"

employee = input("Employee Name: ")

with open(file_path, "a") as file:
    file.write("\n" + employee)

print("Employee saved.")