from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
import os
from typing import List, Optional

app = FastAPI()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI","mongodb+srv://chandansingh639757:<mongodb@cluster0.6txsf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client =  AsyncIOMotorClient(MONGO_URI)
db = client.db
students_collection = db.students

# Pydantic models
class Student(BaseModel):
    name: str = Field(..., description="Name of the student")
    age: int = Field(..., description="Age of the student")
    email: str = Field(..., description="Email address of the student")
    grade: Optional[str] = Field(None, description="Grade of the student")

class StudentResponse(Student):
    id: str = Field(..., description="Student ID")


# Utility function
def format_student(student: dict) -> dict:
    """Convert MongoDB _id to id for API response."""
    student["id"] = str(student["_id"])
    del student["_id"]
    return student
# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Management API"}

# Routes
@app.post("/students", response_model=StudentResponse, status_code=201)
async def create_student(student: Student):
    """Create a new student."""
    student_data = student.dict()
    result = await students_collection.insert_one(student_data)
    created_student = await students_collection.find_one({"_id": result.inserted_id})
    return format_student(created_student)


@app.get("/students/{student_id}", response_model=StudentResponse)
async def get_student(student_id: str):
    """Get a student by ID."""
    student = await students_collection.find_one({"_id": ObjectId(student_id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return format_student(student)


@app.get("/students", response_model=List[StudentResponse])
async def get_all_students():
    """Get all students."""
    students = await students_collection.find().to_list(100)
    return [format_student(student) for student in students]


@app.put("/students/{student_id}", response_model=StudentResponse)
async def update_student(student_id: str, student: Student):
    """Update a student by ID."""
    update_result = await students_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": student.dict()}
    )
    if update_result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    updated_student = await students_collection.find_one({"_id": ObjectId(student_id)})
    return format_student(updated_student)


@app.delete("/students/{student_id}", status_code=204)
async def delete_student(student_id: str):
    """Delete a student by ID."""
    delete_result = await students_collection.delete_one({"_id": ObjectId(student_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return None
