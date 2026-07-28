"""Company Employee Report

Produces a formatted report for employees and company summary.
"""

employees = [
    {"name": "Teja", "department": "Cloud", "salary": 120000},
    {"name": "John", "department": "Security", "salary": 95000},
    {"name": "Alice", "department": "Data", "salary": 110000},
    {"name": "Maria", "department": "DevOps", "salary": 105000},
    {"name": "Rahul", "department": "QA", "salary": 90000},
]


def employee_status(salary):
    """Return status string based on salary threshold."""
    return "Senior Employee" if salary > 100000 else "Growth Path Available"


def print_employee(employee):
    """Print one employee's formatted details."""
    print("=" * 32)
    print()
    print(f"Employee: {employee['name']}")
    print()
    print(f"Department: {employee['department']}")
    print()
    print(f"Salary: ${employee['salary']:,}")
    print()
    print(f"Status: {employee_status(employee['salary'])}")
    print()
    print("=" * 32)


def calculate_average_salary(employees_list):
    """Return average salary (0 if list empty)."""
    total = len(employees_list)
    return sum(e['salary'] for e in employees_list) / total if total else 0


def highest_salary(employees_list):
    """Return highest salary (0 if list empty)."""
    return max((e['salary'] for e in employees_list), default=0)


if __name__ == '__main__':
    # Bonus: sort employees by salary (descending)
    sorted_employees = sorted(employees, key=lambda e: e['salary'], reverse=True)

    for emp in sorted_employees:
        print_employee(emp)

    avg = calculate_average_salary(employees)
    high = highest_salary(employees)

    print()
    print("Company Summary")
    print("-----------------")
    print(f"Total Employees: {len(employees)}")
    print(f"Average Salary: ${avg:,.2f}")
    print(f"Highest Salary: ${high:,.2f}")


