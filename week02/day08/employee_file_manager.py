from pathlib import Path

FILENAME = Path(__file__).resolve().parent / "employees.txt"

while True:
    print("\n" + "1 Add Employee")
    print("2 View Employees")
    print("3 Search Employee")
    print("4 Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Employee Name: ")
        department = input("Department: ")
        salary = input("Salary: ")

        record = f"{name},{department},{salary}\n"

        with open(FILENAME, "a") as file:
            file.write(record)
        print("Employee added.")

    elif choice == "2":
        with open(FILENAME, "r") as file:
            employees = file.read().splitlines()

        if employees:
            for index, employee in enumerate(employees, start=1):
                print(f"Employee {index}: {employee}")
        else:
            print("No employees found.")

    elif choice == "3":
        search_name = input("Search Name: ")
        with open(FILENAME, "r") as file:
            employees = file.read().splitlines()

        found = False
        for employee in employees:
            parts = employee.split(",")
            if len(parts) >= 1:
                name = parts[0].strip()
                if name == search_name:
                    found = True
                    break

        if found:
            print("Employee exists.")
        else:
            print("Employee not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
