from pathlib import Path

file_path = Path(__file__).resolve().parent / "employees.txt"

with open(file_path, "r") as file:
    names = file.read().splitlines()

if names:
    names.pop()

with open(file_path, "w") as file:
    file.write("\n".join(names))

print("Last person removed.")
