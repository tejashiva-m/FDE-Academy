try:
    file = open("employees.txt")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Cleaning up resources.")

    