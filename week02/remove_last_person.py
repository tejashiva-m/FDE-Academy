with open("employees.txt", "r") as file:
    names = file.read().splitlines()

if names:
    names.pop()

with open("employees.txt", "w") as file:
    file.write("\n".join(names))

print("Last person removed.")
