import json
from pathlib import Path

file_path = Path(__file__).resolve().parent / "employees.json"

name = input("Name: ")
department = input("Department: ")
salary = input("Salary: ")

if file_path.exists():
    with file_path.open("r") as file:
        employees = json.load(file)
else:
    employees = []

next_id = max((employee.get("id", 0) for employee in employees), default=0) + 1

new_employee = {
    "id": next_id,
    "name": name,
    "department": department,
    "salary": int(salary)
}

employees.append(new_employee)

with file_path.open("w") as file:
    json.dump(employees, file, indent=4)

print("Employee added with ID", next_id)
