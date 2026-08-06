try:
    from .employee_service import EmployeeService
    from .utils import format_employee, format_header
except ImportError:  # pragma: no cover - allows running the module directly
    from employee_service import EmployeeService
    from utils import format_employee, format_header


class EmployeeDatabaseApp:
    def __init__(self, db_path="company.db"):
        self.service = EmployeeService(db_path)

    def run(self):
        while True:
            print(format_header("Employee Management System"))
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Search Employee")
            print("4. Update Salary")
            print("5. Delete Employee")
            print("6. Search by Department")
            print("7. Sorted by Salary")
            print("8. Show Salary Summary")
            print("9. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self._add_employee()
            elif choice == "2":
                self._view_employees()
            elif choice == "3":
                self._search_employee()
            elif choice == "4":
                self._update_salary()
            elif choice == "5":
                self._delete_employee()
            elif choice == "6":
                self._search_by_department()
            elif choice == "7":
                self._view_sorted_by_salary()
            elif choice == "8":
                self._show_salary_summary()
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

            input("\nPress Enter to continue...")

    def _add_employee(self):
        name = input("Enter employee name: ").strip()
        department = input("Enter department: ").strip()
        salary = int(input("Enter salary: ").strip())
        self.service.create_employee(name, department, salary)
        print("Employee added successfully.")

    def _view_employees(self):
        employees = self.service.list_employees()
        if not employees:
            print("No employees found.")
            return
        print(format_header("Employees"))
        for employee in employees:
            print(format_employee(employee))

    def _search_employee(self):
        name = input("Enter employee name to search: ").strip()
        employees = self.service.search_by_name(name)
        if not employees:
            print("No matching employees found.")
            return
        print(format_header("Search Results"))
        for employee in employees:
            print(format_employee(employee))

    def _update_salary(self):
        employee_id = int(input("Enter employee ID: ").strip())
        salary = int(input("Enter new salary: ").strip())
        self.service.update_salary(employee_id, salary)
        print("Salary updated successfully.")

    def _delete_employee(self):
        employee_id = int(input("Enter employee ID: ").strip())
        self.service.delete_employee(employee_id)
        print("Employee deleted successfully.")

    def _search_by_department(self):
        department = input("Enter department name: ").strip()
        employees = self.service.search_by_department(department)
        if not employees:
            print("No matching employees found.")
            return
        print(format_header("Employees by Department"))
        for employee in employees:
            print(format_employee(employee))

    def _view_sorted_by_salary(self):
        employees = self.service.list_employees_sorted_by_salary()
        print(format_header("Employees by Salary"))
        for employee in employees:
            print(format_employee(employee))

    def _show_salary_summary(self):
        print(format_header("Salary Summary"))
        print(f"Average salary: ${self.service.get_average_salary():,.2f}")
        print(f"Highest salary: ${self.service.get_highest_salary():,.0f}")
        departments = []
        for employee in self.service.list_employees():
            departments.append(employee.department)
        unique_departments = sorted(set(departments))
        print("Employees by department:")
        for department in unique_departments:
            print(f"- {department}: {self.service.count_by_department(department)}")

    def close(self):
        self.service.close()


if __name__ == "__main__":
    app = EmployeeDatabaseApp()
    try:
        app.run()
    finally:
        app.close()
