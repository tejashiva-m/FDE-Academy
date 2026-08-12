# Day 19: Automated API Testing

## What we are testing

The test suite covers the full employee API:

- `POST /employees`
- `GET /employees`
- `GET /employees/{id}`
- `PUT /employees/{id}`
- `DELETE /employees/{id}`
- Request validation failures (`422`)
- Missing employees (`404`)
- Duplicate email conflicts (`409`)

## How the tests work

```text
test_employees.py -> TestClient -> FastAPI -> employee_service -> SQLite
```

`TestClient` sends requests directly to the FastAPI application. It does not
start a real web server, and we do not need to open Swagger.

Each test receives a fresh temporary SQLite database through a pytest fixture.
This keeps tests independent and prevents them from changing `employees.db`.

## Arrange, Act, Assert

Most tests follow three simple steps:

1. **Arrange** the input data and any existing employee.
2. **Act** by calling an endpoint with `TestClient`.
3. **Assert** the status code and response body.

## Run the project

```bash
cd day19
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Swagger is available at `http://127.0.0.1:8000/docs` while the server runs.

## Run the tests

```bash
cd day19
source .venv/bin/activate
pytest -v
```

For a shorter output, run `pytest -q`.
