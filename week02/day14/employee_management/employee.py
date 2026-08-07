from dataclasses import dataclass
from typing import Optional


@dataclass
class Employee:
    id: Optional[int]
    name: str
    department: str
    salary: int