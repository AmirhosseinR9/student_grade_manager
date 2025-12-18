# Student Grade Manager

A simple Python console-based application for managing student records and their scores.
The project uses a modular structure, basic object-oriented design, and JSON file storage
to persist data between runs.

## Features

- Add and delete students
- Add and remove scores for each student
- Calculate average score dynamically
- View all students and their scores
- Input validation for names and scores
- Persistent storage using a JSON file
- Clear separation of logic and data handling

## Project Structure

student_grade_manager/ │ ├─ main.py               # Application entry point and menu logic ├─ README.md             # Project documentation └─ src/ ├─ student.py         # Student class and related logic └─ storage.py         # Load/save data from JSON file

## How to Run

1. Clone the repository:
   `bash
   git clone https://github.com/your-username/student_grade_manager.git

2. Navigate to the project directory:

cd student_grade_manager


3. Run the program:

python main.py



Data Storage

All student data is automatically saved in a JSON file. Changes such as adding or removing students or scores are persisted between runs.

Design Notes

The Student class represents the data model.

The average score is calculated dynamically and is not stored.

File handling logic is separated from business logic.

No external libraries are used.


Future Improvements

Add unit tests

Add sorting and filtering options

Replace JSON storage with a database

Build a simple GUI or web interface


License

This project is licensed under the MIT License.

---
