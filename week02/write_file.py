employee = input("Employee Name: ")

with open("employees.txt", "a") as file:
    file.write("\n" + employee)

print("Employee saved.")