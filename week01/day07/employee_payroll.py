import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

MAX_SALARY = 1_000_000


class PromotionError(ValueError):
    pass


class Employee:

    def __init__(self, name: str, department: str, salary: float) -> None:
        self.name = name
        self.department = department
        self.salary = salary

    def display(self) -> None:
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:,.2f}")

    def annual_bonus(self) -> float:
        return self.salary * 0.10

    def promote(self, raise_amount: float) -> None:
        try:
            if self.salary < 0:
                raise PromotionError("Salary cannot be negative.")
            if self.salary > MAX_SALARY:
                raise PromotionError("Salary exceeds company policy.")
            if raise_amount <= 0:
                raise PromotionError("Raise amount must be positive.")

            self.salary += raise_amount
            logging.info("Employee promoted.")
            print("Promotion successful.")

        except PromotionError as error:
            logging.error("Promotion rejected.")
            print(f"Promotion failed: {error}")


if __name__ == "__main__":
    employee = Employee("Teja", "Cloud", 120000)
    employee.display()

    employee.promote(10000)

    employee.promote(-5000)
    employee.promote(2_000_000)
