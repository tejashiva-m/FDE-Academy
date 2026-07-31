with open("employees.txt", "r") as file:
    employees = file.read().splitlines()

for index, employee in enumerate(employees, start=1):
    print(f"Employee {index}: {employee}")

