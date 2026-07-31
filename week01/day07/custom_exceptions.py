class SalaryTooHighError(Exception):
    pass

MAX_SALARY = 1_000_000

def validate_salary(salary):

    if salary > MAX_SALARY:
        raise SalaryTooHighError(
            "Salary exceeds company policy."
        )