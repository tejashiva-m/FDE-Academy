from company import Company
from employee import Employee
from intern import Intern
from manager import Manager

people = [
    Employee("Alice", "Cloud", 120000),
    Employee("Diana", "Engineering", 95000),
    Manager("Bob", "Cloud", 150000, 6),
    Manager("Eve", "Operations", 170000, 10),
    Intern("Charlie", "Cloud", 30000, "UT Dallas"),
    Intern("Frank", "Design", 28000, "UT Austin"),
]

for person in people:
    person.display()

print("\nPolymorphism bonus salaries:")
for person in people:
    print(person.annual_bonus())

company = Company("OpenAI")
for person in people:
    company.add_employee(person)

print("\nCompany Summary")
company.display_summary()
