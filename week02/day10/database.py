import json
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "employees.json"


def load_database():
    if not DB_PATH.exists():
        return []

    with DB_PATH.open("r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_database(employees):
    with DB_PATH.open("w") as file:
        json.dump(employees, file, indent=4)


def get_next_id(employees):
    existing_ids = [employee.get("id", 0) for employee in employees]
    return max(existing_ids, default=0) + 1
