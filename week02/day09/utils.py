def format_currency(amount):
    return f"${amount:,.2f}"


def employee_status(salary):
    return "Senior Employee" if salary > 100000 else "Growth Path Available"
