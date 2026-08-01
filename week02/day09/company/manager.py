from .employee import Employee


class Manager(Employee):

    def __init__(self, name, department, salary, team_size):
        super().__init__(name, department, salary)
        self.team_size = team_size

    def display(self):
        super().display()
        print(f"Team Size: {self.team_size}")

    def annual_bonus(self):
        return self.salary * 0.20

