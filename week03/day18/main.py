import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

try:
    from .database import initialize_database
    from .employee_service import (
        create_employee,
        delete_employee,
        get_employee,
        get_employees,
        update_employee,
    )
except ImportError:  # pragma: no cover - allows direct execution
    from database import initialize_database
    from employee_service import (
        create_employee,
        delete_employee,
        get_employee,
        get_employees,
        update_employee,
    )

initialize_database()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=2)
    department: str = Field(min_length=2)
    salary: float = Field(gt=0)
    email: EmailStr


class EmployeeUpdate(BaseModel):
    name: str = Field(min_length=2)
    department: str = Field(min_length=2)
    salary: float = Field(gt=0)
    email: EmailStr


class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str
    salary: float
    email: EmailStr


@app.get("/employees", response_model=list[EmployeeResponse])
def list_employees():
    return get_employees()


@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def read_employee(employee_id: int):
    employee = get_employee(employee_id)
    if employee is None:
        logger.warning("Employee %s not found", employee_id)
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.post("/employees", response_model=EmployeeResponse, status_code=201)
def add_employee(employee: EmployeeCreate):
    try:
        employee_id = create_employee(
            name=employee.name,
            department=employee.department,
            salary=employee.salary,
            email=str(employee.email),
        )
    except ValueError as exc:
        logger.warning("Duplicate employee creation attempted: %s", exc)
        raise HTTPException(status_code=409, detail="Employee already exists") from exc
    except Exception as exc:  # pragma: no cover - defensive logging path
        logger.exception("Unexpected error while creating employee")
        raise HTTPException(status_code=500, detail="Internal server error") from exc

    logger.info("Employee %s created", employee_id)
    return {"id": employee_id, **employee.model_dump(), "email": str(employee.email)}


@app.put("/employees/{employee_id}", response_model=EmployeeResponse)
def replace_employee(employee_id: int, employee: EmployeeUpdate):
    existing = get_employee(employee_id)
    if existing is None:
        logger.warning("Employee %s not found for update", employee_id)
        raise HTTPException(status_code=404, detail="Employee not found")

    try:
        updated = update_employee(
            employee_id,
            name=employee.name,
            department=employee.department,
            salary=employee.salary,
            email=str(employee.email),
        )
    except ValueError as exc:
        logger.warning("Duplicate employee update attempted: %s", exc)
        raise HTTPException(status_code=409, detail="Employee already exists") from exc
    except Exception as exc:  # pragma: no cover - defensive logging path
        logger.exception("Unexpected error while updating employee")
        raise HTTPException(status_code=500, detail="Internal server error") from exc

    logger.info("Employee %s updated", employee_id)
    return updated


@app.delete("/employees/{employee_id}", status_code=204)
def remove_employee(employee_id: int):
    deleted = delete_employee(employee_id)
    if not deleted:
        logger.warning("Employee %s not found for deletion", employee_id)
        raise HTTPException(status_code=404, detail="Employee not found")

    logger.info("Employee %s deleted", employee_id)
