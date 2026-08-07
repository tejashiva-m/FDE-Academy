def employee_status(salary):
    if salary >= 120000:
        return "Senior Employee"
    if salary >= 80000:
        return "Mid-Level Employee"
    return "Junior Employee"


def format_employee(employee):
    return (
        f"ID: {employee.id}\n\n"
        f"Name: {employee.name}\n\n"
        f"Department: {employee.department}\n\n"
        f"Salary: ${employee.salary:,.0f}\n\n"
        f"Status: {employee_status(employee.salary)}"
    )


def format_reports(report_data):
    lines = []
    for title, value in report_data.items():
        lines.append(f"{title}: {value}")
    return "\n".join(lines)
