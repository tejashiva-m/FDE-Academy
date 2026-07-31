with open("employees.txt") as file:

    for line in file:
        print(line.strip())

# Strip() is used to remove any leading or trailing whitespace characters, including newlines, from each line before printing it.   