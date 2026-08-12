from pydantic import BaseModel, ConfigDict, EmailStr, Field


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    department: str = Field(min_length=1, max_length=100)
    salary: float = Field(gt=0)


class EmployeeUpdate(EmployeeCreate):
    pass


class EmployeeResponse(EmployeeCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
