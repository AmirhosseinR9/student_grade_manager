import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from student import Student
from storage import load_students, save_students, add_student, delete_student

def get_scores():
    
    scores = []

    while True:
        try:
            count = int(input("How many scores? "))
            if count <= 0:
                print("Count must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    for i in range(count):
        while True:
            try:
                score = float(input(f"Score {i+1}: "))
                if 0 < score <= 20:
                    scores.append(score)
                    break
                else:
                    print("The score must be between 0 and 20.")
                    continue   
            except ValueError:
                print("Please enter a valid number.")

    return scores


def menu():
    print("\n--- Student Manager ---")
    print("1. Add student")
    print("2. Delete student")
    print("3. Show student")
    print("4. Show all students")
    print("5. Add score student")
    print("6. Remove score student")
    print("0. Exit")


def main():
    students = load_students()

    while True:
        menu()
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        # Add student
        if choice == 1:
            name = input("Name: ").strip()
            scores = get_scores()
            student = Student(name, scores)

            if add_student(students, student):
                save_students(students)
                print("Student added.")
            else:
                print("This student already exists.")

        # Delete student
        elif choice == 2:
            name = input("Name to delete: ").strip()
            if delete_student(students, name):
                save_students(students)
                print("Student deleted.")
            else:
                print("Student not found.")

        # Show student
        elif choice == 3:
            name = input("Name to show: ").strip()
            student = students.get(name)
            if student is None:
                print("Student not found.")
            else:
                print(f"Name: {student.name}")
                print(f"Scores: {student.scores}")
                print(f"Average: {student.average}")

        # Show all
        elif choice == 4:
            if not students:
                print("No students in the system.")
            else:
                for st in students.values():
                    print(f"- {st.name} | Scores: {st.scores} | Avg: {st.average}")

        elif choice == 5:
            name = input("Name: ").strip()
            if name in students:
                while True:
                    try:
                        score = float(input(f"Score: "))
                        if 0 < score <= 20:
                            break
                        else:
                            print("The score must be between 0 and 20.")
                            continue   
                    except ValueError:
                        print("Please enter a valid number.")
                
                student = students[name]
                student.add_score(score)
                save_students(students)
                print("Score added")
                    
            else:
                print("Student not found.")


        elif choice == 6:
            name = input("Name: ").strip()
            if name in students:
                student = students[name]
                student.print_scores()
                while True:
                    try:
                        index = int(input("Enter score number to remove: ")) - 1
                        if index < 0 or index >= len(student.scores):
                            print("Please enter the correct score.")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Invalid number")
                        continue

                student.remove_score(index)
                save_students(students)
                print("Score removed")
                
            else:    
                print("Student not found.")

        elif choice == 0:
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()