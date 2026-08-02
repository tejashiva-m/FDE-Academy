import json

employee = {
    "name": "Alice",
    "department": "Security",
    "salary": 95000
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

print("JSON saved.")

