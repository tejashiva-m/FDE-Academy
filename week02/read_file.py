with open("employees.txt", "r") as file:
    content = file.read()

print(content)

with open("employees.txt", "r") as file:
    content = file.readlines()

print(content)