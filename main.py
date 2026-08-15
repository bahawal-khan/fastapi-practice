from fastapi import FastAPI, HTTPException
from typing import List
from schemas import Student, StudentUpdate, StudentResponse
import json

app = FastAPI()


# ==========================
# GET All Students
# ==========================
@app.get("/students", response_model=List[StudentResponse])
def get_students():
    with open("students.json", "r") as file:
        students = json.load(file)

    return students


# ==========================
# GET Student By ID
# ==========================
@app.get("/student/{id}", response_model=StudentResponse)
def get_student_by_id(id: int):

    with open("students.json", "r") as file:
        students = json.load(file)

    for student in students:
        if student["id"] == id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# ==========================
# POST Create Student
# ==========================
@app.post("/student", response_model=StudentResponse)
def create_student(student: Student):

    with open("students.json", "r") as file:
        students = json.load(file)

    students.append(student.model_dump())

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    return student


# ==========================
# Demo Response Model
# ==========================
@app.get("/student/demo", response_model=StudentResponse)
def get_demo():

    return {
        "id": 1,
        "name": "Ali",
        "age": 23,
        "email": "ali@gmail.com",
        "password": "123456"
    }


# ==========================
# PUT (Complete Update)
# ==========================
@app.put("/student/{id}", response_model=StudentResponse)
def update_student(id: int, student: StudentUpdate):

    with open("students.json", "r") as file:
        students = json.load(file)

    for i, std in enumerate(students):

        if std["id"] == id:

            students[i]["name"] = student.name
            students[i]["age"] = student.age
            students[i]["course"] = student.course
            students[i]["email"] = student.email
            students[i]["gender"] = student.gender
            students[i]["role"] = student.role

            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)

            return students[i]

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# ==========================
# PATCH (Partial Update)
# ==========================
@app.patch("/student/{id}")
def patch_student(id: int, student: StudentUpdate):

    with open("students.json", "r") as file:
        students = json.load(file)

    for s in students:

        if s["id"] == id:

            if student.name is not None:
                s["name"] = student.name

            if student.age is not None:
                s["age"] = student.age


            if student.email is not None:
                s["email"] = student.email

            if student.gender is not None:
                s["gender"] = student.gender

            
            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)

            return {
                "message": "Student updated successfully",
                "student": s
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
## delete

@app.delete("/student/{id}")
def delete_student(id: int):

    with open("students.json", "r") as file:
        students = json.load(file)

    for i, student in enumerate(students):

        if student["id"] == id:

            students.pop(i)

            with open("students.json", "w") as file:
                json.dump(students, file, indent=4)

            return {
                "message": "Data deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )



@app.post("/student", response_model=StudentResponse)
def create_student(student: Student):

    with open("students.json", "r") as file:
        students = json.load(file)

    students.append(student.model_dump())

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

    return student
    
        

