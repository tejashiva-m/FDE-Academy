from pathlib import Path

file_path = Path(__file__).resolve().parent / "employees.txt"

with open(file_path, "r") as file:
    employees = file.read().splitlines()

for index, employee in enumerate(employees, start=1):
    print(f"Employee {index}: {employee}")

