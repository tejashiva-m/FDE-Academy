employees = ["Teja", "John", "Alice"]

for index, employee in enumerate(employees):
    print(index, employee)

print()

for index, employee in enumerate(employees, start=1):
    print(index, employee)


