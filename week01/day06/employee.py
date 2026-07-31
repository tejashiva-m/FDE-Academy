MAX_SALARY = 1_000_000


class Employee:
    """Base class for all employees."""

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def employee_status(self):
        if self.salary > 100000:
            return "Senior Employee"
        else:
            return "Growth Path Available"

    def display(self):
        print("=" * 40)
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:,.2f}")
        print(f"Status: {self.employee_status()}")
        print("=" * 40)

    def annual_bonus(self):
        return self.salary * 0.10

    def promote(self, raise_amount):
        if not isinstance(raise_amount, (int, float)):
            raise TypeError("raise_amount must be a number")
        if raise_amount <= 0:
            raise ValueError("raise_amount must be positive")
        new_salary = self.salary + raise_amount
        if new_salary > MAX_SALARY:
            raise ValueError("promotion would exceed maximum allowed salary")
        print(f"Promoting {self.name}: +${raise_amount:,}")
        self.salary = new_salary

        