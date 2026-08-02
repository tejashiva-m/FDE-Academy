import json
from pathlib import Path

file_path = Path(__file__).resolve().parent / "employees.json"

name = input("Name: ")
department = input("Department: ")
salary = input("Salary: ")

new_employee = {
    "name": name,
    "department": department,
    "salary": int(salary)
}

if file_path.exists():
    with file_path.open("r") as file:
        employees = json.load(file)
else:
    employees = []

employees.append(new_employee)

with file_path.open("w") as file:
    json.dump(employees, file, indent=4)

print("Employee added.")
