from fastapi import FastAPI

app = FastAPI()

sample_employees = [
    {"id": 1, "name": "Teja", "department": "Cloud", "salary": 120000},
    {"id": 2, "name": "Asha", "department": "Engineering", "salary": 95000},
    {"id": 3, "name": "Ben", "department": "Sales", "salary": 80000},
]


@app.get("/")
def home():
    return {"message": "Welcome to my first FastAPI application!"}


@app.get("/employees")
def get_employees():
    return sample_employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in sample_employees:
        if employee["id"] == employee_id:
            return employee
    return {"detail": "Employee not found"}


@app.get("/search")
def search_employees(department: str):
    matches = [employee for employee in sample_employees if employee["department"].lower() == department.lower()]
    return matches


@app.get("/company")
def company_info():
    return {
        "company": "OpenAI",
        "employees": 120,
        "departments": 5,
        "location": "Dallas",
    }


@app.get("/status")
def status():
    return {
        "application": "running",
        "version": "1.0.0",
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/employee")
def employee():
    return {
        "name": "Teja",
        "department": "Cloud",
        "salary": 120000,
    }

@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return {
        "employee_id": employee_id
    }

@app.get("/search")
def search(name: str):
    return {
        "search": name
    }

