from typing import Optional

from fastapi import FastAPI, HTTPException, Query

try:
    from .database import initialize_database
    from .employee_service import create_employee, delete_employee, get_employee, get_employees, update_employee
except ImportError:  # pragma: no cover - allows direct execution
    from database import initialize_database
    from employee_service import create_employee, delete_employee, get_employee, get_employees, update_employee

initialize_database()

app = FastAPI()


@app.get("/employees")
def list_employees(
    department: Optional[str] = Query(default=None),
    min_salary: Optional[float] = Query(default=None),
):
    return get_employees(department=department, min_salary=min_salary)


@app.get("/employees/{employee_id}")
def read_employee(employee_id: int):
    employee = get_employee(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.post("/employees", status_code=201)
def add_employee(payload: dict):
    if not payload.get("name") or not str(payload["name"]).strip():
        raise HTTPException(status_code=400, detail="Name is required")
    if payload.get("salary") is None:
        raise HTTPException(status_code=400, detail="Salary is required")

    employee_id = create_employee(
        name=str(payload["name"]).strip(),
        department=str(payload.get("department", "")).strip(),
        salary=float(payload["salary"]),
    )
    return {"id": employee_id, **payload}


@app.put("/employees/{employee_id}")
def replace_employee(employee_id: int, payload: dict):
    employee = get_employee(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    updated = update_employee(
        employee_id,
        name=payload.get("name"),
        department=payload.get("department"),
        salary=payload.get("salary"),
    )
    return updated


@app.delete("/employees/{employee_id}")
def remove_employee(employee_id: int):
    deleted = delete_employee(employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted"}
