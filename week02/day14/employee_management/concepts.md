# Dataclasses

## What is @dataclass?
@dataclass is a Python decorator that automatically creates common methods for a class, such as __init__, __repr__, and __eq__. It helps reduce repetitive boilerplate code.

## Why use dataclasses?
Dataclasses make it easier to create simple classes that store data. They keep the code shorter and easier to read.

## Difference between a normal class and a dataclass?
A normal class usually requires you to write methods like __init__ manually. A dataclass generates those methods automatically, so it is faster to write and easier to maintain.

# SQL

## What does GROUP BY do?
GROUP BY groups rows that have the same value in one or more columns so you can summarize them together.

## What is AVG()?
AVG() calculates the average value of a numeric column.

## What is COUNT()?
COUNT() returns the number of rows that match a query or a group.

## What is MAX()?
MAX() returns the largest value in a column.

## What is MIN()?
MIN() returns the smallest value in a column.

# Architecture

## Why separate database.py from employee_service.py?
Separating them keeps database connection logic and business logic in different places. This makes the code easier to maintain and reuse.

## What is Separation of Concerns?
Separation of Concerns means each module should focus on one responsibility. The database module handles storage, while the service module handles employee operations.

## Why shouldn't SQL be inside main.py?
SQL should not be inside main.py because the main file should focus on user interaction. Keeping SQL in the service layer makes the app cleaner, easier to test, and easier to change later.