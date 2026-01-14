from fastapi import FastAPI, HTTPException
from typing import List
from .models import Student, StudentCreate
from .storage import load_students, save_students

app = FastAPI()

students = load_students()

def next_id():
    return max([s["id"] for s in students], default=0) + 1

@app.get("/students/", response_model=List[Student])
def get_students():
    return students

@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    for s in students:
        if s["id"] == student_id:
            return s
    raise HTTPException(status_code=404, detail="Schüler nicht gefunden")

@app.post("/students/", response_model=Student)
def create_student(student: StudentCreate):
    new_student = student.dict()
    new_student["id"] = next_id()
    students.append(new_student)
    save_students(students)
    return new_student

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentCreate):
    for s in students:
        if s["id"] == student_id:
            s.update(student.dict())
            save_students(students)
            return s
    raise HTTPException(status_code=404, detail="Schüler nicht gefunden")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            save_students(students)
            return {"message": "Schüler gelöscht"}
    raise HTTPException(status_code=404, detail="Schüler nicht gefunden")

@app.get("/initialize/")
def initialize():
    global students
    students = [
        {
            "id": 1,
            "name": "Max Mustermann",
            "birth_date": "2006-05-01",
            "entry_date": "2021-09-01",
            "class_name": "5AHINF"
        },
        {
            "id": 2,
            "name": "Anna Berger",
            "birth_date": "2005-11-12",
            "entry_date": "2020-09-01",
            "class_name": "6BHINF"
        },
        {
            "id": 3,
            "name": "Lukas Maier",
            "birth_date": "2007-02-20",
            "entry_date": "2022-09-01",
            "class_name": "4CHINF"
        }
    ]
    save_students(students)
    return {"message": "Beispieldaten erstellt"}
