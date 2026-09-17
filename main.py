from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

class Student(BaseModel):
    student_fname: str
    student_lname: str
    student_phone_number: str
    student_parent_phone_number: str
    student_address: str
    student_email: str
    
database={}
student_counter=1
app=FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True)

@app.post("/student")
def create_student(student: Student):
    global student_counter
    database[student_counter]= student
    student_counter+=1
    return "Student created successfully!"
@app.get("/student")
def get_students():
    return database
@app.get("/student/{student_id}")
def get_student(student_id: int):
    if student_id in database:
        return database[student_id]
    raise HTTPException(status_code=404, detail="Student not found")
@app.put("/student/{student_id}")
def update_student(student_id:int, student: Student):
    if student_id in database:
        database[student_id]= student
        return "Student updated successfully!"
    raise HTTPException(status_code=404, detail="Student not found")
@app.delete("/student/{student_id}")
def delete_student(student_id:int):
    if student_id in database:
        del database[student_id]
        return "Student deleted successfully!"