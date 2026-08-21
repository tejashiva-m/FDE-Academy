import sqlite3

import employee_service
from database import get_db
from fastapi import Depends, FastAPI, HTTPException, Response, status
from schemas import EmployeeCreate, EmployeeResponse, EmployeeUpdate

app = FastAPI(title="Employee API", version="1.0.0")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_employee(
    employee: EmployeeCreate,
    connection: sqlite3.Connection = Depends(get_db),
):
    try:
        return employee_service.create_employee(connection, employee)
    except sqlite3.IntegrityError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An employee with this email already exists",
        ) from error


@app.get("/employees", response_model=list[EmployeeResponse])
def list_employees(connection: sqlite3.Connection = Depends(get_db)):
    return employee_service.list_employees(connection)


@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    connection: sqlite3.Connection = Depends(get_db),
):
    employee = employee_service.get_employee(connection, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    connection: sqlite3.Connection = Depends(get_db),
):
    try:
        updated_employee = employee_service.update_employee(
            connection, employee_id, employee
        )
    except sqlite3.IntegrityError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An employee with this email already exists",
        ) from error

    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee


@app.delete("/employees/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(
    employee_id: int,
    connection: sqlite3.Connection = Depends(get_db),
):
    if not employee_service.delete_employee(connection, employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
