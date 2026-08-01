from pathlib import Path

file_path = Path(__file__).resolve().parent / "employees.txt"

with open(file_path) as file:

    for line in file:
        print(line.strip())

# Strip() is used to remove any leading or trailing whitespace characters, including newlines, from each line before printing it.   