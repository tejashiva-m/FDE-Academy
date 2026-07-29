from employee import Employee


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def average_salary(self):
        return sum(e.salary for e in self.employees) / len(self.employees) if self.employees else 0

    def highest_salary(self):
        return max(e.salary for e in self.employees) if self.employees else 0

    def display_all(self):
        print("\n" + "#" * 8 + f" {self.name} " + "#" * 8)
        for e in self.employees:
            e.display()
        print()
        print("Company Summary")
        print(f"Total Employees: {len(self.employees)}")
        print(f"Average Salary: ${self.average_salary():,.2f}")
        print(f"Highest Salary: ${self.highest_salary():,.2f}")


if __name__ == '__main__':
    employees = [
        Employee("Teja", "Cloud", 120000),
        Employee("John", "Security", 95000),
        Employee("Alice", "Data", 110000),
        Employee("Maria", "DevOps", 105000),
        Employee("Rahul", "QA", 90000),
    ]

    # Loop and display each employee
    for emp in employees:
        emp.display()

    # Summary calculations
    total = len(employees)
    average = sum(e.salary for e in employees) / total if total else 0
    highest = max(e.salary for e in employees) if employees else 0

    print()
    print("Company Summary")
    print(f"Total Employees: {total}")
    print(f"Average Salary: ${average:,.2f}")
    print(f"Highest Salary: ${highest:,.2f}")

    # Bonus: use Company class
    company = Company("Acme Corp")
    for e in employees:
        company.add_employee(e)
    # company.display_all()
