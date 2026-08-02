import json
from pathlib import Path

from database import load_database, save_database
from utils import employee_status


def input_employee():
    name = input("Name: ")
    department = input("Department: ")
    salary = int(input("Salary: "))
    return {"name": name, "department": department, "salary": salary}


def find_employee_by_name(employees, name):
    for employee in employees:
        if employee.get("name", "").lower() == name.strip().lower():
            return employee
    return None


def export_senior_employees(employees):
    senior_employees = [
        employee for employee in employees if employee.get("salary", 0) > 100000
    ]
    export_path = Path(__file__).resolve().parent / "senior_employees.json"
    with export_path.open("w") as file:
        json.dump(senior_employees, file, indent=4)
    print(f"Exported {len(senior_employees)} senior employees to senior_employees.json")


def main():
    while True:
        print("\n1 Add Employee")
        print("2 View Employees")
        print("3 Search Employee")
        print("4 Update Salary")
        print("5 Delete Employee")
        print("6 Exit")
        print("7 Export Senior Employees")

        choice = input("Choose an option: ")
        employees = load_database()

        if choice == "1":
            new_employee = input_employee()
            employees.append(new_employee)
            save_database(employees)
            print("Employee added.")

        elif choice == "2":
            if not employees:
                print("No employees found.")
                continue

            for employee in employees:
                print("\nName:", employee.get("name"))
                print("Department:", employee.get("department"))
                print("Salary:", employee.get("salary"))
                print("Status:", employee_status(employee.get("salary", 0)))

        elif choice == "3":
            search_name = input("Employee Name: ")
            employee = find_employee_by_name(employees, search_name)
            if employee:
                print("Employee Found")
                print("Department:", employee.get("department"))
                print("Salary:", employee.get("salary"))
            else:
                print("Employee not found.")

        elif choice == "4":
            search_name = input("Employee Name: ")
            employee = find_employee_by_name(employees, search_name)
            if employee:
                new_salary = int(input("New Salary: "))
                employee["salary"] = new_salary
                save_database(employees)
                print("Salary updated.")
            else:
                print("Employee not found.")

        elif choice == "5":
            search_name = input("Employee Name: ")
            employee = find_employee_by_name(employees, search_name)
            if employee:
                employees.remove(employee)
                save_database(employees)
                print("Employee deleted.")
            else:
                print("Employee not found.")

        elif choice == "6":
            print("Goodbye!")
            break

        elif choice == "7":
            confirm = input("Export senior employees? (y/n): ")
            if confirm.strip().lower() == "y":
                export_senior_employees(employees)
            else:
                print("Export canceled.")

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
