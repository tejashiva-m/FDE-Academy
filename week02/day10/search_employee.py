import json
from pathlib import Path

file_path = Path(__file__).resolve().parent / "employees.json"

employee_name = input("Employee Name: ")

with file_path.open("r") as file:
    employees = json.load(file)

found = False
for employee in employees:
    if employee.get("name", "").lower() == employee_name.strip().lower():
        print("Employee Found")
        print(f"Department: {employee.get('department')}")
        print(f"Salary: {employee.get('salary')}")
        found = True
        break

if not found:
    print("Employee not found.")
