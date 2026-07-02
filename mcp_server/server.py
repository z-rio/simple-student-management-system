import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


sys.path.insert(0, str(BASE_DIR))

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")  
django.setup()

from mcp.server.fastmcp import FastMCP
from students import services
 
mcp = FastMCP("Student Management")

def student_to_dict(student):
    return {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "age": student.age,
        "created_at": student.created_at.isoformat(),
        "updated_at": student.updated_at.isoformat()
    }

@mcp.tool()
def count_students() -> int:
    return services.count_students()

@mcp.tool()
def get_student_by_id(student_id: int) -> dict:
    student = services.get_student_by_id(student_id)
    if student:
        return student_to_dict(student)
    return None

@mcp.tool()
def create_student(name: str, email: str, age: int) -> dict:
    student = services.create_student(name, email, age)
    return student_to_dict(student)

@mcp.tool()
def delete_student(student_id: int) -> bool:
    return services.delete_student(student_id)

@mcp.tool()
def search_student_by_name(name: str) -> list:
    students = services.search_student_by_name(name)
    return [
        student_to_dict(student) for student in students
    ]

@mcp.tool()
def update_student(student_id: int, name: str = None, email: str = None, age: int = None) -> dict:
    student = services.update_student(student_id, name, email, age)

    if student is None:
        return {
            "error": "Student not found"
        }

    return student_to_dict(student)

    """
    Update one or more fields for an existing student.

    Any field left as None will remain unchanged.
    """


if __name__ == "__main__":
    mcp.run()






