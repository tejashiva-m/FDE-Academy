import json

with open("employee.json") as file:
    employee = json.load(file)

print(employee)

print(employee["name"])
print(employee["department"])
print(employee["salary"])