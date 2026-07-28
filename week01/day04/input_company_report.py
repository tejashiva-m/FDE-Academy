def employee_status(salary):
    return "Senior Employee" if salary > 100000 else "Growth Path Available"


def print_employee(employee):
    print("=" * 32)
    print(f"Employee: {employee['name']}")
    print(f"Department: {employee['department']}")
    print(f"Salary: ${employee['salary']:,}")
    print(f"Status: {employee_status(employee['salary'])}")
    print("=" * 32)


def calculate_average_salary(employees):
    return sum(emp['salary'] for emp in employees) / len(employees) if employees else 0


def highest_salary(employees):
    return max(emp['salary'] for emp in employees) if employees else 0


def collect_employees():
    employees = []
    while True:
        name = input("Enter employee name (or type done): ").strip()
        if name.lower() == "done":
            break
        department = input("Enter department: ").strip()
        salary_input = input("Enter salary: ").strip()

        try:
            salary = int(salary_input)
        except ValueError:
            print("Please enter a valid number for salary.")
            continue

        employees.append({
            "name": name,
            "department": department,
            "salary": salary,
        })

    return employees


def print_summary(employees):
    print("\nCompany Summary")
    print(f"Total Employees: {len(employees)}")
    print(f"Average Salary: ${calculate_average_salary(employees):,.2f}")
    print(f"Highest Salary: ${highest_salary(employees):,.2f}")


if __name__ == '__main__':
    employees = collect_employees()
    if not employees:
        print("No employees were entered.")
    else:
        for employee in employees:
            print_employee(employee)
        print_summary(employees)
