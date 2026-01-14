from pydantic import BaseModel
from datetime import date

class Student(BaseModel):
    id: int
    name: str
    birth_date: date
    entry_date: date
    class_name: str

class StudentCreate(BaseModel):
    name: str
    birth_date: date
    entry_date: date
    class_name: str
