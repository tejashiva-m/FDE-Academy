import sqlite3

try:
    from .employee_service import (
        add_employee,
        delete_employee,
        export_employees,
        get_all_employees,
        get_average_salary,
        get_department_breakdown,
        get_department_count,
        get_employee_count,
        get_highest_salary,
        get_lowest_salary,
        search_employee,
        update_salary,
    )
    from .utils import format_employee, format_reports
except ImportError:  # pragma: no cover - allows direct execution
    from employee_service import (
        add_employee,
        delete_employee,
        export_employees,
        get_all_employees,
        get_average_salary,
        get_department_breakdown,
        get_department_count,
        get_employee_count,
        get_highest_salary,
        get_lowest_salary,
        search_employee,
        update_salary,
    )
    from utils import format_employee, format_reports


def show_reports():
    report_data = {
        "Average Salary": f"${get_average_salary():,.2f}",
        "Highest Salary": f"${get_highest_salary():,.0f}",
        "Lowest Salary": f"${get_lowest_salary():,.0f}",
        "Employee Count": get_employee_count(),
        "Department Count": get_department_count(),
    }
    print("\nReports")
    print("-" * 30)
    print(format_reports(report_data))
    print("\nDepartment Breakdown")
    print("-" * 30)
    for department, count in get_department_breakdown():
        print(f"{department}: {count}")


def main():
    while True:
        print("\n1 Add Employee")
        print("2 View Employees")
        print("3 Search Employee")
        print("4 Update Salary")
        print("5 Delete Employee")
        print("6 Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                name = input("Enter employee name: ").strip()
                department = input("Enter department: ").strip()
                salary = float(input("Enter salary: ").strip())
                add_employee(name, department, salary)
                export_employees()
                print("Employee added successfully.")
            elif choice == "2":
                employees = get_all_employees()
                if not employees:
                    print("No employees found.")
                else:
                    for employee in employees:
                        print("\n" + format_employee(employee))
                show_reports()
            elif choice == "3":
                keyword = input("Enter name or department to search: ").strip()
                employees = search_employee(keyword)
                if not employees:
                    print("No employees found.")
                else:
                    for employee in employees:
                        print("\n" + format_employee(employee))
            elif choice == "4":
                employee_id = int(input("Enter employee ID: ").strip())
                salary = float(input("Enter new salary: ").strip())
                updated = update_salary(employee_id, salary)
                export_employees()
                print("Salary updated." if updated else "Employee not found.")
            elif choice == "5":
                employee_id = int(input("Enter employee ID: ").strip())
                deleted = delete_employee(employee_id)
                export_employees()
                print("Employee deleted." if deleted else "Employee not found.")
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid menu choice.")
        except ValueError as exc:
            print(f"Input error: {exc}")
        except sqlite3.Error as exc:
            print(f"Database error: {exc}")
        except RuntimeError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()