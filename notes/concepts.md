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


