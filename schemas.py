from pydantic import BaseModel, Field
from typing import Optional, Literal


# ==========================
# POST (Create Student)
# ==========================
class Student(BaseModel):
    id: int = Field(..., description="The ID of the student")
    name: str = Field(
        min_length=3,
        max_length=20,
        description="The name of the student"
    )
    age: int = Field(
        gt=0,
        lt=120,
        description="The age of the student"
    )
    course: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=20,
        description="The course of the student"
    )
    email: Optional[str] = Field(
        default=None,
        description="The email of the student"
    )
    gender: Literal["male", "Female"] = Field(
        ...,
        description="The gender of the student"
    )
    role: Optional[Literal["student", "teacher"]] = Field(
        default=None,
        description="The role of the user"
    )


# ==========================
# PUT & PATCH (Update Student)
# ==========================
class StudentUpdate(BaseModel):
    name: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=20
    )
    age: Optional[int] = Field(
        default=None,
        gt=0,
        lt=120
    )
    course: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=20
    )
    email: Optional[str] = Field(default=None)
    gender: Optional[Literal["male", "Female"]] = Field(default=None)
    role: Optional[Literal["student", "teacher"]] = Field(default=None)


# ==========================
# Response Model
# ==========================
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int