from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3004"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

students = []

@app.get("/students")
def get_students():
    return students

@app.post("/students")
def add_student(student: dict):
    print("RECEIVED:", student)
    students.append(student)
    return {"message": "Student added", "data": student}