# Purpose: Print employee details and summary statistics.

# def print_employee(employee):
#     ...

# def print_summary(employees):
#     ...

# def employee_status(salary):
#     ...

employees = [
    {"name": "Teja", "department": "Cloud", "salary": 120000},
    {"name": "John", "department": "Security", "salary": 95000},
]


def employee_status(salary):
    """Return status string based on salary."""
    return "Senior Employee" if salary > 100000 else "Growth Path Available"


def print_employee(employee):
    """Print a single employee's formatted details."""
    print("=" * 32)
    print(f"Employee: {employee['name']}")
    print(f"Department: {employee['department']}")
    print(f"Salary: ${employee['salary']:,}")
    print(f"Status: {employee_status(employee['salary'])}")
    print("=" * 32)


def print_summary(employees):
    """Print summary statistics for the employee list."""
    total = len(employees)
    average = sum(e['salary'] for e in employees) / total if total else 0
    highest = max(e['salary'] for e in employees) if employees else 0

    print()
    print(f"Total Employees: {total}")
    print(f"Average Salary: ${average:,.2f}")
    print(f"Highest Salary: ${highest:,.2f}")


if __name__ == '__main__':
    for emp in employees:
        print_employee(emp)
    print_summary(employees)

    
