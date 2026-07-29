from employee import Employee


class Company:

    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_summary(self):
        print(f"Company Name: {self.name}")
        print(f"Total Employees: {len(self.employees)}")

        if self.employees:
            salaries = [employee.salary for employee in self.employees]
            average_salary = sum(salaries) / len(salaries)
            highest_salary = max(salaries)
            manager_count = sum(1 for employee in self.employees if employee.__class__.__name__ == "Manager")
            intern_count = sum(1 for employee in self.employees if employee.__class__.__name__ == "Intern")

            print(f"Average Salary: ${average_salary:,.2f}")
            print(f"Highest Salary: ${highest_salary:,.2f}")
            print(f"Managers: {manager_count}")
            print(f"Interns: {intern_count}")
        else:
            print("Average Salary: $0.00")
            print("Highest Salary: $0.00")
            print("Managers: 0")
            print("Interns: 0")
