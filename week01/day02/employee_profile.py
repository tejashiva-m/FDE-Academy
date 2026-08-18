# Requirements:
# Ask for:
# Name
# Department
# Salary
# Years of Experience

# Create a function that prints a nicely formatted employee profile.

# Bonus challenge: If the salary is greater than $100,000, print: Senior Employee
# Otherwise: Growth Path Available

def print_employee_profile(name, department, salary, years_of_experience):
    print(f"\n{'=' * 32}")
    print("Employee Profile")
    print(f"{'=' * 32}")
    print(f"Name: {name}")
    print(f"Department: {department}")
    print(f"Salary: ${salary}")
    print(f"Years of Experience: {years_of_experience}")

    if salary > 100000:
        print("Status: Senior Employee")
    else:
        print("Status: Growth Path Available")
    
    print(f"{'=' * 32}\n")

print_employee_profile("Teja", "FDE", 120000, 5)
