Student Grade Manager
A simple console-based Python project for managing students and their grades. This project is designed for learning and practicing core Python concepts such as functions, classes, file handling, and basic data persistence using JSON.
Features
Add new students
Delete existing students
Add grades to a student
Remove a specific grade from a student
Calculate student average grades dynamically
Save and load data using a JSON file
Project Structure
student_grade_manager/ ├── main.py ├── README.md ├── src/ │ ├── student.py │ └── storage.py 
File Description
main.py
Entry point of the program. Handles user interaction and menu logic.
src/student.py
Contains the Student class. Responsible for student data, grade operations, and average calculation.
src/storage.py
Handles loading and saving student data to a JSON file.
How It Works
Student data is stored in memory as a dictionary: { "student_name": Student_object } 
Data is persisted in a students.json file.
The average grade is calculated dynamically and is never stored directly.
Requirements
Python 3.8 or higher
No external libraries required
