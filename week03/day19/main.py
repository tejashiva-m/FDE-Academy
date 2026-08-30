import employee_service
import psycopg
from database import get_db
from fastapi import Depends, FastAPI, HTTPException, Response, status
from health import router as health_router
from schemas import EmployeeCreate, EmployeeResponse, EmployeeUpdate

app = FastAPI(title="Employee API", version="1.0.0")
db_dependency = Depends(get_db)

app.include_router(health_router)


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
    connection=db_dependency,
):
    try:
        return employee_service.create_employee(connection, employee)
    except psycopg.IntegrityError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An employee with this email already exists",
        ) from error


@app.get("/employees", response_model=list[EmployeeResponse])
def list_employees(connection=db_dependency):
    return employee_service.list_employees(connection)


@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(
    employee_id: int,
    connection=db_dependency,
):
    employee = employee_service.get_employee(connection, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    connection=db_dependency,
):
    try:
        updated_employee = employee_service.update_employee(
            connection, employee_id, employee
        )
    except psycopg.IntegrityError as error:
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
    connection=db_dependency,
):
    if not employee_service.delete_employee(connection, employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
