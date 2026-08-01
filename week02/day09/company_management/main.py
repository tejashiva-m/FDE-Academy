from .employee import Employee
from .manager import Manager
from .intern import Intern


def main():
    people = [
        Employee("Teja", "Cloud", 120000),
        Employee("Sravanti", "Engineering", 95000),
        Manager("Alice", "Cloud", 150000, 8),
        Manager("Rahul", "Product", 140000, 6),
        Intern("Bob", "Cloud", 30000, "UT Dallas"),
        Intern("Meera", "Design", 28000, "NYU"),
        Employee("Arun", "Support", 85000),
    ]

    for person in people:
        person.display()
        print(f"Annual Bonus: {person.annual_bonus():,.2f}")
        print()


if __name__ == "__main__":
    main()
