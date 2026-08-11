# HTTP Status Codes

## What does 200 mean?
200 means the request was successful and the server returned the requested information.

## What does 201 mean?
201 means a new resource was successfully created.

## What does 204 mean?
204 means the request succeeded, but there is no response body to return.

## What does 400 mean?
400 means the client sent a bad request.

## What does 404 mean?
404 means the requested resource was not found.

## What does 409 mean?
409 means the request conflicts with the current state of the server, such as trying to create a duplicate record.

## What does 422 mean?
422 means the request body is syntactically valid but fails validation rules.

## What does 500 mean?
500 means the server encountered an unexpected internal error.

## Why shouldn't "employee not found" return 200?
It should not return 200 because the operation did not succeed in the way the client expected. A missing resource should be reported as a failure with a 404 status.

# HTTPException

## What is HTTPException?
HTTPException is FastAPI's built-in way to return an HTTP error response with a specific status code and message.

## Why use HTTPException instead of returning an error dictionary?
HTTPException is better because it uses the correct HTTP status code and creates a standard error response that clients and tools can understand.

# Business Errors

## What is the difference between validation failure and business conflict?
A validation failure means the request does not match the expected schema or rules. A business conflict means the data is valid, but it conflicts with a rule in the application, such as trying to create a duplicate employee.

## Why would a duplicate employee be a 409 instead of a 422?
A duplicate employee is a 409 because the request is structurally valid, but it conflicts with the current data state.

# Error Handling

## Why shouldn't we catch every exception with except Exception?
Catching every exception hides important details and makes debugging harder. It is better to handle known cases explicitly and let unexpected errors surface for logging and fixes.

## Why is logging important when an API fails?
Logging is important because it helps developers understand what went wrong and where the problem happened.

# API Reliability

## Why should APIs have predictable error responses?
Predictable error responses make APIs easier for clients, testers, and developers to understand and consume consistently.

## What would you include in a standard API error response?
A standard API error response should include an error code, a human-readable message, and often a request id or timestamp.
