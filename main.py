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