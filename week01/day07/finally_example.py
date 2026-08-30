try:
    with open("employees.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Cleaning up resources.")
    