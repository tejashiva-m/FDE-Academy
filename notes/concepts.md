# Variables

Variables store values in memory.

Good variable names explain what they contain.

Examples:

customer_name

invoice_total

current_role

Avoid:

x

abc

temp1

# Strings
name = "    Teja    "

print(name)
print(name.strip())

Output:

'    Teja    '
'Teja'     #spaces will be removed from the above input when we use strip.


**print(name.strip())**

strip() removes extra spaces (or specified characters) from the beginning and end of a string. It is commonly used to clean user input before processing it.

**print(name.startswith("T"))**

startswith() returns True if the string begins with the specified value; otherwise it returns False.

**print(name.endswith("a"))**

endswith() returns True if the string ends with the specified value; otherwise it returns False.


# Operators:

print(10 / 5)
print(10 // 3)
print(10 % 3)

What is the difference between / and //?
Single forward slash is which exactly divides the integer with decimal and give that in decimal value.  Double forward slash will give dividend like 10 // 3 = 3 is the dividend and 1 is the remainder

When would % be useful?

% will help us only get the reminder as output value after dividing the integer. 

# Lists:

employees.insert(1, "David")
The above logic will insert David string at the location 1 that is next to first integer.

**employees.sort()**

It will sort the strings given by naming order from A to Z

**employees.reverse()**

This logic will reverse the above order and provide the output from Z to A.

# Tuples:
We cannot change the data in the tuples, meaning we cannot modify the existing given tuple with other assigning value.  

# Dictionary vs List

if you frequently retrieve items by a known key, prefer dict; if you need ordering, indexing, or duplicates, prefer list.

Dict is something we lookup for fast access and list is making a list or sequence order of list.

# Sets

When we use sets the duplicates will be automatically removed. 

# loops

1:
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number * 2)

2:
print(10 * 2)
print(20 * 2)
print(30 * 2)

Why is 1st better than 2nd one:

Because for higher numbers more than 100000 the for loop will be easier syntax and execution process rather than assigning it individually one by one. 

# Enumerate:

What is the meaning of enumerate in Python?
In Python, `enumerate` is a built-in function that adds a counter to an iterable (like a list or tuple) and returns it as an enumerate object. This allows you to loop through the iterable while keeping track of the index of each item. 

# While Loop

count = 1

while count <= 5:
    print(count)
    count += 1

OP: 1 2 3 4 5 

print()

 count = 1

  while count <= 5:
     print(count)

OP: infinite loop

If you miss count += 1 it will start repeating 1 until we stop with Ctrl + C. This is called an infinite loop. 

# Break & Continue:

Question:

What's the difference?

The difference between `break` and `continue` in a loop is how they affect the flow of the loop:
- `break`: When the `break` statement is encountered, it immediately terminates the loop, and the program continues executing the code that follows the loop. In the first example, when `number` equals 5, the loop stops executing, and no further numbers are printed.
- `continue`: When the `continue` statement is encountered, it skips the rest of the code inside the loop for the current iteration and moves on to the next iteration of the loop. In the second example, when `number` equals 5, the `continue` statement causes the loop to skip printing that number and move on to the next iteration, so all numbers except 5 are printed.

# Refactoring

Refactoring means reorganizing and cleaning up code without changing what it does. It makes the code easier to read, maintain, and extend.

Why are functions better than writing everything in one file?

Functions let you name pieces of behavior and reuse them. They make code easier to understand because each function has a single job. When the program grows, functions help avoid repeating the same code and make it easier to fix bugs or add new features.


# Dict vs Class Instances

- Structure: a `dict` is a built-in mapping of keys to values (e.g. `{"name": "Teja"}`); an instance like `Employee(...)` is an object of a user-defined class with named attributes.
- Behavior: `dict` stores data only; a class can include methods, validation, and computed properties (data + behavior together).
- Readability & tooling: classes (and `@dataclass`) give clearer intent, type hints, and better IDE completion; dicts are lightweight but less explicit.
- Use cases: use a `dict` for quick scripts or dynamic records; use a class when you need abstraction, invariants, or reusable behavior.
- Interop: dicts serialize to JSON easily; classes can provide `to_dict()` / `from_dict()` helpers or be converted using `dataclasses.asdict()`.

Example:

```
employee = {"name": "Teja"}

from dataclasses import dataclass

@dataclass
class Employee:
    name: str

emp = Employee("Teja")
```

Summary: start with dicts for small tasks; prefer classes/dataclasses as the program grows and you need structure, methods, or validation.

# Object-Oriented Programming

What is a class?

A class is a blueprint or template that defines the structure and behavior (attributes and methods) of a kind of object. Think of it as the recipe; each object made from the class follows that recipe.

What is an object?

An object (or instance) is a concrete value created from a class. Each object has its own attribute values but shares the same behavior defined by the class.

What is `__init__`?

`__init__` is a special method that runs automatically when you create an instance. It initializes the object's attributes (its starting state).

What is `self`?

`self` is the reference to the instance inside class methods. Use `self` to read or write the instance's attributes and to call other methods on the same object.

Why are methods useful?

Methods bundle behavior with the data they operate on. They let objects perform actions, keep code organized, and encapsulate logic (validation, state changes) close to the data.

Why use a class instead of a dictionary?

- Classes group data and behavior together, making code clearer when objects need rules or methods.
- Classes can enforce invariants and validation in one place.
- Classes support type hints, IDE help, and can implement special methods (`__str__`, `__repr__`, comparison operators).
- Dicts are lighter and fine for simple or temporary records, but classes scale better for complex logic.

# Modules & Packages

What is a module?
A module is a single Python file that contains code, such as functions, classes, or variables. It groups related behavior together so other programs can import and reuse it.

What is a package?
A package is a folder that contains Python modules and an `__init__.py` file. It allows multiple modules to be organized in a directory and imported with a common package name.

Why split code into multiple files?
Splitting code into multiple files keeps each part focused on one responsibility. It makes the code easier to read, test, and maintain, and prevents one large file from getting too complicated.

Difference between:

`import module`
- Loads the whole module under its name.
- You use the module name before the function or class, for example `module.function()`.
- This helps avoid name conflicts and makes it clear where each symbol comes from.

`from module import function`
- Loads a specific function, class, or variable directly into the current file.
- You can use it without the module prefix, for example `function()`.
- This is useful when you only need a few names and want shorter code.

What is `__init__.py`?
`__init__.py` is a file that tells Python a directory should be treated as a package. It often imports package symbols or sets up package-level logic.

What is `__name__`?
`__name__` is a special variable that tells you how a Python file is being used. If the file is run directly, `__name__` is set to `"__main__"`. If it is imported, `__name__` is set to the module path.

Why use `if __name__ == "__main__"`?
This condition lets a file act both as a reusable module and as a script. Code inside that block runs only when the file is executed directly, not when it is imported.

Why create utility modules?
Utility modules store helper functions that are used across multiple files. They reduce code repetition, keep shared logic in one place, and make it easier to update behavior consistently.

# Import Statements

`import calculator`
- Loads the module named `calculator`.
- You access functions or variables with the module name, for example `calculator.add(2, 3)`.
- This is useful when you want to keep the module namespace clear and avoid naming collisions.

`from calculator import add`
- Loads only the name `add` from the `calculator` module into the current namespace.
- You can call it directly as `add(2, 3)` without the module prefix.
- This is useful when you only need a specific function or want shorter code.

Key difference:
- `import calculator` keeps the full module namespace.
- `from calculator import add` brings a specific name directly into your code.

Research note — `__str__`:

Many classes define `__str__()` to return a human-friendly string representation of an object. This makes printing or logging instances more readable (e.g., `print(employee)` shows useful info instead of a generic object address).

# Inheritance

Inheritance lets one class reuse the behavior and data of another class. A Manager and an Intern can both use the basic employee information from Employee without rewriting it every time.

Why use inheritance?

Inheritance helps avoid duplicate code, keeps shared behavior in one place, and makes it easier to expand the program with new employee types later.

What is `super()`?

`super()` lets a child class call the parent class's initializer or methods. It is useful when the child wants to reuse the parent setup before adding its own details.

# Method Overriding

Method overriding happens when a child class provides its own version of a method that already exists in the parent class. For example, Manager and Intern can override `display()` so they add their own extra information.

# Polymorphism

Polymorphism means “many forms.” The same method name can behave differently depending on the object that calls it. In this project, calling `display()` on an Employee, a Manager, and an Intern each shows the right behavior for that object.

# Composition

Composition means building a class from other objects rather than inheriting everything. A Company is a good example because it can contain many employee objects inside a list.

HAS-A vs IS-A

- IS-A means inheritance. A Manager IS an Employee.
- HAS-A means composition. A Company HAS many employees.

`isinstance()` is a helpful tool when we need to check the type of an object. For example, `isinstance(employee, Manager)` checks whether the object is a Manager or a subclass of Manager. This is more reliable than checking a department string because it uses actual object type instead of a value that could be changed or mistyped.

# Exception Handling

What is an exception?

An exception is an error that happens while a program is running. Python raises exceptions to tell us that something unexpected happened, such as invalid input or an impossible calculation.

Why use try?

`try` lets us test code that might fail without stopping the whole program. It gives us a safe place to handle problems.

Why use except?

`except` lets us respond to errors in a controlled way. Instead of the program crashing, we can show a friendly message or take another path.

Why use finally?

`finally` runs no matter what happens. It is useful for cleanup tasks like closing files or database connections.

What does raise do?

`raise` is used to trigger an exception manually. This is helpful when we want to stop a process and show a meaningful error message.

Why create custom exceptions?

Custom exceptions make errors more specific and easier to understand. Instead of using a general error for everything, we can create a clear exception for a specific rule.

Why use logging instead of print?

Logging is better than `print()` because it is easier to organize, easier to control, and better for larger programs. Logging can show different levels of importance, and it is more professional for real applications.

# Reading Files

`read()` returns the entire file as one string.

`readlines()` returns the file as a list of lines, where each line keeps its newline character unless we strip it.

When we use `read()`, the output is a single block of text. When we use `readlines()`, the output is a list of separate lines, which makes it easier to loop through each line one by one.

# File Handling

What is a file?

A file is a stored collection of data on disk. We can use files to save information such as employee names, department names, or salaries so the data stays available even after the program closes.

Why use files?

Files are useful because they let us keep data between program runs. Instead of losing information when the program stops, we can read and write it from a file.

Difference between:

- `read()` reads the whole file as one string.
- `readline()` reads one line at a time.
- `readlines()` reads all lines and returns them as a list.

Why use `with open()`?

`with open()` is a safer way to work with files because it closes the file automatically when we are done, even if an error happens.

Why use append mode (`"a"`)?

Append mode adds new data to the end of the file without deleting what is already there. That is useful for building a list of employees over time.

What does `strip()` remove?

`strip()` removes extra spaces, tabs, or newlines from the beginning and end of a string. It helps clean up user input and file content.

Why catch `FileNotFoundError`?

`FileNotFoundError` happens when we try to read a file that does not exist. Catching it helps us show a friendly message instead of letting the program crash.

