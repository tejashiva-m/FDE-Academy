from dataclasses import dataclass


@dataclass
class Employee:
    id: int | None
    name: str
    department: str
    salary: int