from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, computed_field
from pathlib import Path
import json

app = FastAPI()

# -----------------------------
# File setup
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "raw.json"


# -----------------------------
# Helper functions
# -----------------------------
def show():
    """Read data from JSON file"""
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]")  # empty list

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def dump(data):
    """Write data to JSON file"""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# -----------------------------
# Pydantic Model
# -----------------------------
class Student(BaseModel):
    id: int
    name: str
    age: int
    city: str
    height: float  # meters
    weight: int    # kg

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 3)


# -----------------------------
# Create Student
# -----------------------------
@app.post("/post")
def create_student(upload: Student):
    data = show()

    # check duplicate ID
    for item in data:
        if item["id"] == upload.id:
            raise HTTPException(
                status_code=400,
                detail="ID already exists"
            )

    new_student = upload.model_dump()
    data.append(new_student)

    dump(data)

    return {
        "message": "Student created successfully",
        "data": new_student
    }


# -----------------------------
# Get All Students
# -----------------------------
@app.get("/students")
def get_students():
    return show()


# -----------------------------
# Get Student by ID
# -----------------------------
@app.get("/students/{student_id}")
def get_student(student_id: int):
    data = show()

    for item in data:
        if item["id"] == student_id:
            return item

    raise HTTPException(status_code=404, detail="Student not found")


# -----------------------------
# Delete Student
# -----------------------------
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    data = show()

    new_data = [item for item in data if item["id"] != student_id]

    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="Student not found")

    dump(new_data)

    return {"message": "Student deleted successfully"}