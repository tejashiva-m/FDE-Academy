
from fastapi import FastAPI, HTTPException, Query

try:
    from .database import initialize_database
    from .employee_service import (
        create_employee,
        delete_employee,
        get_employee,
        get_employees,
        update_employee,
    )
    from .schemas import EmployeeCreate, EmployeeResponse, EmployeeUpdate
except ImportError:  # pragma: no cover - allows direct execution
    from database import initialize_database
    from employee_service import (
        create_employee,
        delete_employee,
        get_employee,
        get_employees,
        update_employee,
    )
    from schemas import EmployeeCreate, EmployeeResponse, EmployeeUpdate

initialize_database()

app = FastAPI()


@app.get("/employees", response_model=list[EmployeeResponse])
def list_employees(
    department: str | None = Query(default=None),
    min_salary: float | None = Query(default=None),
):
    return get_employees(department=department, min_salary=min_salary)


@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def read_employee(employee_id: int):
    employee = get_employee(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.post("/employees", response_model=EmployeeResponse, status_code=201)
def add_employee(employee: EmployeeCreate):
    employee_id = create_employee(
        name=employee.name,
        department=employee.department,
        salary=employee.salary,
        email=employee.email,
    )
    return {"id": employee_id, **employee.model_dump()}


@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def replace_employee(employee_id: int, employee: EmployeeUpdate):
    existing = get_employee(employee_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    updated = update_employee(
        employee_id,
        name=employee.name,
        department=employee.department,
        salary=employee.salary,
        email=employee.email,
    )
    return updated


@app.delete("/employees/{employee_id}")
def remove_employee(employee_id: int):
    deleted = delete_employee(employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted"}
