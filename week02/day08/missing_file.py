from pathlib import Path

file_path = Path(__file__).resolve().parent / "abc.txt"

try:

    with open(file_path) as file:
        print(file.read())

except FileNotFoundError:
    print("File doesn't exist.")

