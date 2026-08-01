from pathlib import Path

file_path = Path(__file__).resolve().parent / "employees.txt"

with open(file_path, "r") as file:
    content = file.read()

print(content)

with open(file_path, "r") as file:
    content = file.readlines()

print(content)