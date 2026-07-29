from employee import Employee


class Intern(Employee):

    def __init__(
        self,
        name,
        department,
        salary,
        university
    ):
        super().__init__(name, department, salary)
        self.university = university

    def display(self):
        super().display()
        print(f"University: {self.university}")

    def annual_bonus(self):
        return 0
