from pydantic import BaseModel, Field, EmailStr


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

