from employee import Employee
from manager import Manager
from intern import Intern


employees = [
    Employee("Alice", "Cloud", 120000),
    Manager("Bob", "Cloud", 150000, 6),
    Intern("Charlie", "Cloud", 30000, "UT Dallas"),
]

for person in employees:
    person.display()
