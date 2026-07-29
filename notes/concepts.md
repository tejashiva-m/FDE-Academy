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

