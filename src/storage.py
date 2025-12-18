import json
import os
from student import Student

DATA_FILE = "students.json"


def load_students():
    
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    students = {}
    for name, data in raw.items():
        students[name] = Student.from_dict(data)

    return students


def save_students(students):

    out = {}

    for name, student in students.items():
        out[name] = student.to_dict()

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


def add_student(students, student: Student):
    
    if student.name in students:
        return False

    students[student.name] = student
    return True


def delete_student(students, name):
    
    return students.pop(name, None) is not None