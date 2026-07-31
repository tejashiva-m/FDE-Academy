try:

    with open("abc.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("File doesn't exist.")

