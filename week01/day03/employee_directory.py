# ================================
# Employee: Teja

# Department: Cloud

# Salary: $120,000

# Status: Senior Employee
# ================================
# If salary > 100000
# Senior Employee
# Else
# Growth Path Available

# At the end, print:
# Total Employees: 2
# At the end, print:
# Average Salary: $107,500.00
# Highest Salary: $120,000.00

employees = [
    {
        "name": "Teja",
        "department": "Cloud",
        "salary": 120000
    },
    {
        "name": "John",
        "department": "Security",
        "salary": 95000
    }
]

print("=" * 32)
for employee in employees:
    print(f"Employee: {employee['name']}\n")
    print(f"Department: {employee['department']}\n")
    print(f"Salary: ${employee['salary']:,}\n")
    
    if employee['salary'] > 100000:
        print("Status: Senior Employee\n")
    else:
        print("Status: Growth Path Available\n")
print("=" * 32)

average_salary = sum(emp['salary'] for emp in employees) / len(employees)
highest_salary = max(emp['salary'] for emp in employees)

print(f"Total Employees: {len(employees)}")
print(f"Average Salary: ${average_salary:,.2f}")
print(f"Highest Salary: ${highest_salary:,.2f}")    





