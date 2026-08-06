def format_employee(employee):
    return f"ID: {employee.id} | Name: {employee.name} | Department: {employee.department} | Salary: ${employee.salary:,.0f}"


def format_header(title):
    return f"\n{'=' * 40}\n{title}\n{'=' * 40}"
