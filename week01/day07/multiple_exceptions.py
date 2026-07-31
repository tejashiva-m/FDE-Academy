try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

