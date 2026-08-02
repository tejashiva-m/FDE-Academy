import json

with open("employees.json") as file:
    employees = json.load(file)

for employee in employees:
    print(employee["name"])