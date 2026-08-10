# Pydantic

## What is Pydantic?
Pydantic is a Python library that validates and parses data using models. It helps make sure the data sent to an API matches the rules we define.

## Why does FastAPI use Pydantic?
FastAPI uses Pydantic so request and response data can be validated automatically. This makes APIs safer and easier to understand.

## What is a Pydantic model?
A Pydantic model is a class that describes the structure of data and the rules for that data. For example, a model can require a name, department, and salary.

## What is the difference between a request model and a response model?
A request model describes what the client is allowed to send to the API. A response model describes what the API will return.

## What happens when invalid data reaches an API?
When invalid data reaches an API, FastAPI rejects it before the business logic or database layer can use it. This prevents bad data from entering the system.

## What is an API contract?
An API contract is the agreement between the client and the API about what data is accepted and what data is returned.

## What does Field(gt=0) mean?
Field(gt=0) means the value must be greater than zero.

## What does Field(min_length=2) mean?
Field(min_length=2) means the string must have at least two characters.

## Why should validation happen before database operations?
Validation should happen before database operations because it prevents invalid or unsafe data from reaching the database and keeps the system more reliable.

## Why is centralized validation important in large systems?
Centralized validation is important because it creates consistent rules across the whole application. This reduces mistakes and makes it easier for many developers to work together.
