employee = {
    "name": "Teja",
    "role": "Senior DevOps Engineer",
    "experience": 11,
    "cloud": "Azure"
}

print(employee["name"])
print(employee["role"])

employee["salary"] = 120000

print(employee)

print(employee.keys())
print(employee.values())
print(employee.items())

for key, value in employee.items():
    print(f"{key}: {value}")