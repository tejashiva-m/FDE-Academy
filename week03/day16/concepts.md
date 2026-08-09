# FastAPI + Database

FastAPI communicates with SQLite by receiving HTTP requests, passing the request data into Python functions, and then using the service layer to run SQL statements against the database.

## What is a service layer?
A service layer is a middle layer between the API and the database. It keeps the business logic organized and makes the code easier to maintain.

## Why shouldn't SQL queries be directly inside main.py?
SQL should not be inside main.py because main.py should focus on handling requests. Keeping SQL in a service layer improves clarity, reusability, and testability.

## What is dependency separation?
Dependency separation means each part of the application has a clear responsibility. The API handles requests, the service layer handles logic, and the database layer handles storage.

## What happens when a POST request reaches FastAPI?
When a POST request reaches FastAPI, the request body is read, the route function processes the data, and the service layer inserts the new record into the database.

## What happens when a GET request reaches FastAPI?
When a GET request reaches FastAPI, the route reads the URL parameters, calls the service layer, and returns the matching data from the database as a JSON response.

## What happens when a DELETE request reaches FastAPI?
When a DELETE request reaches FastAPI, the route identifies the target record, the service layer removes it from the database, and the API returns a success response.

## What is persistence?
Persistence means data is stored in a durable form so it survives after the program stops running.

## Why is database persistence better than storing data in Python variables?
Database persistence is better because data remains available across app restarts, multiple requests, and different program runs. Python variables only hold data temporarily in memory.

Client
  ↓
FastAPI
  ↓
Service Layer
  ↓
Database Layer
  ↓
SQLite
