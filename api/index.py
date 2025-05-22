from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks data
data_path = os.path.join(os.path.dirname(__file__), "..", "q-vercel-python.json")
with open(data_path, "r") as f:
    students = json.load(f)

# Convert list to dictionary for fast lookup
student_dict = {student["name"]: student["marks"] for student in students}

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/api")
def get_marks(name: List[str] = []):
    result = [student_dict.get(n, 0) for n in name]
    return {"marks": result}
