# CSC1024 Programming Principles - Final Project
# Python-Powered Student Grading System

import os
import re

# -- Constants for filenames --
STUDENTS_FILE = 'students.txt'
COURSES_FILE = 'courses.txt'
GRADES_FILE = 'grades.txt'

# -- Helper Functions --

def initialize_files():
    """Create data files if they don't exist to prevent file not found errors."""
    for filename in [STUDENTS_FILE, COURSES_FILE, GRADES_FILE]:
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                pass  # Create an empty file

def is_valid_email(email):
    """Simple regex for email validation."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_course_name(name):
    """Ensures course name contains only alphabetic characters and spaces."""
    return re.match(r"^[a-zA-Z\s]+$", name)

def get_non_empty_input(prompt):
    """Ensures that user input is not empty."""
    user_input = ""
    while not user_input:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
    return user_input

def get_numeric_input(prompt):
    """Ensures that user input is a valid number and rounds to two decimal places."""
    while True:
        try:
            user_input = float(get_non_empty_input(prompt))
            if 0 <= user_input <= 100:
                return round(user_input, 2)
            else:
                print("Marks should be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(marks):
    """Calculates the letter grade based on marks."""
    if marks >= 80:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 50:
        return 'D'
    else:
        return 'F'

def student_exists(student_id):
    """Check if a student ID already exists in the system."""
    with open(STUDENTS_FILE, 'r') as f:
        for line in f:
            if line.strip().split(',')[0] == student_id:
                return True
    return False

def course_exists(course_id):
    """Check if a course ID already exists in the system."""
    with open(COURSES_FILE, 'r') as f:
        for line in f:
            if line.strip().split(',')[0].upper() == course_id.upper():
                return True
    return False

# -- Core Functionality --

def add_student():
    """Adds a new student to the students.txt file."""
    print("\n--- Add a New Student ---")
    student_id = get_non_empty_input("Enter Student ID: ")
    if student_exists(student_id):
        print("Error: Student ID already exists.")
        return
        
    name = get_non_empty_input("Enter Student Name: ")
    
    email = ""
    while not is_valid_email(email):
        email = get_non_empty_input("Enter Student Email: ")
        if not is_valid_email(email):
            print("Invalid email format. Please try again.")

    with open(STUDENTS_FILE, 'a') as f:
        f.write(f"{student_id},{name},{email}\n")
    print("Student added successfully!")

def add_course():
    """Adds a new course to the courses.txt file."""
    print("\n--- Add a New Course ---")
    course_id = get_non_empty_input("Enter Course ID: ").upper()
    if course_exists(course_id):
        print("Error: Course ID already exists.")
        return
        
    course_name = ""
    while not is_valid_course_name(course_name):
        course_name = get_non_empty_input("Enter Course Name: ")
        if not is_valid_course_name(course_name):
            print("Invalid course name. Course name can only contain alphabetic characters and spaces.")

    with open(COURSES_FILE, 'a') as f:
        f.write(f"{course_id},{course_name}\n")
    print("Course added successfully!")

def update_course():
    """Updates an existing course's name."""
    print("\n--- Update Course ---")
    course_id = get_non_empty_input("Enter Course ID to update: ").upper()
    if not course_exists(course_id):
        print("Error: Course ID not found.")
        return

    new_course_name = get_non_empty_input("Enter New Course Name: ")

    try:
        with open(COURSES_FILE, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No courses found.")
        return

    updated_lines = []
    record_updated = False
    for line in lines:
        cid, name = line.strip().split(',', 1) # Split only on the first comma
        if cid == course_id:
            updated_lines.append(f"{course_id},{new_course_name}\n")
            record_updated = True
        else:
            updated_lines.append(line)

    if record_updated:
        with open(COURSES_FILE, 'w') as f:
            f.writelines(updated_lines)
        print("Course updated successfully!")
    else:
        # This case should ideally not be reached due to the initial course_exists check
        print("Error: Course not found for update.")

def delete_course():
    """Deletes a course and all associated grades."""
    print("\n--- Delete Course ---")
    course_id = get_non_empty_input("Enter Course ID to delete: ").upper()
    if not course_exists(course_id):
        print("Error: Course ID not found.")
        return

    # Check for associated grades
    grades_found = False
    grade_lines = []
    try:
        with open(GRADES_FILE, 'r') as f:
            grade_lines = f.readlines()
            for line in grade_lines:
                sid, cid, _, _ = line.strip().split(',')
                if cid.upper() == course_id:
                    grades_found = True
                    break
    except FileNotFoundError:
        pass # No grades file means no associated grades

    if grades_found:
        print(f"Warning: This course has associated grades. Deleting this course will also delete all grades for {course_id}.")
        confirmation = get_non_empty_input("Are you sure you want to proceed? (yes/no): ").lower()
        if confirmation != 'yes':
            print("Course deletion cancelled.")
            return

    # Delete course from courses.txt
    try:
        with open(COURSES_FILE, 'r') as f:
            course_lines = f.readlines()
    except FileNotFoundError:
        course_lines = [] # Should not happen due to course_exists check

    updated_course_lines = [line for line in course_lines if line.strip().split(',')[0].upper() != course_id]
    with open(COURSES_FILE, 'w') as f:
        f.writelines(updated_course_lines)

    # Delete associated grades from grades.txt
    if grades_found:
        updated_grade_lines = [line for line in grade_lines if line.strip().split(',')[1].upper() != course_id]
        with open(GRADES_FILE, 'w') as f:
            f.writelines(updated_grade_lines)
        print(f"Course {course_id} and all associated grades deleted successfully!")
    else:
        print(f"Course {course_id} deleted successfully!")

def record_student_marks():
    """Records or updates marks for a student in a specific course."""
    print("\n--- Record Student Marks ---")
    student_id = get_non_empty_input("Enter Student ID: ")
    if not student_exists(student_id):
        print("Error: Student ID not found.")
        return

    course_id = get_non_empty_input("Enter Course ID: ").upper()
    if not course_exists(course_id):
        print("Error: Course ID not found.")
        return

    try:
        with open(GRADES_FILE, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    record_found = False
    found_index = -1
    for i, line in enumerate(lines):
        sid, cid, _, _ = line.strip().split(',')
        if sid == student_id and cid.upper() == course_id:
            record_found = True
            found_index = i
            break
    
    marks = get_numeric_input("Enter Marks (0-100): ")
    grade = calculate_grade(marks)
    new_record = f"{student_id},{course_id},{marks:.2f},{grade}\n"

    if record_found:
        # Extract existing marks to format with % for display
        _, _, existing_marks_str, existing_grade = lines[found_index].strip().split(',')
        print(f"The record for this subject already exists! The current record is: {student_id},{course_id},{float(existing_marks_str):.2f}%,{existing_grade}")
        update_choice = get_non_empty_input(f"Do you want to update to the new record ({student_id},{course_id},{marks:.2f}%,{grade})? (yes/no): ").lower()
        if update_choice == 'yes':
            lines[found_index] = new_record
            with open(GRADES_FILE, 'w') as f:
                f.writelines(lines)
            print("Record updated successfully!")
        else:
            print("Update cancelled.")
    else:
        with open(GRADES_FILE, 'a') as f:
            f.write(new_record)
        print("Marks recorded successfully!")

def display_student_performance():
    """Displays the performance report for a single student."""
    print("\n--- Display Individual Student Performance ---")
    student_id = get_non_empty_input("Enter Student ID to view report: ")
    if not student_exists(student_id):
        print("Error: Student ID not found.")
        return

    print(f"\nPerformance Report for Student ID: {student_id}")
    print("-" * 50)
    found_grades = False
    with open(GRADES_FILE, 'r') as f:
        for line in f:
            sid, course_id, marks, grade = line.strip().split(',')
            if sid == student_id:
                print(f"Course: {course_id}, Marks: {float(marks):.2f}%, Grade: {grade}")
                found_grades = True
    
    if not found_grades:
        print("No grades recorded for this student yet.")
    print("-" * 50)


def display_course_performance():
    """Displays the performance summary for a specific course."""
    print("\n--- Display Course Performance Summary ---")
    course_id = get_non_empty_input("Enter Course ID to view summary: ").upper()
    if not course_exists(course_id):
        print("Error: Course ID not found.")
        return

    print(f"\nPerformance Summary for Course ID: {course_id}")
    print("-" * 50)
    
    student_grades = []
    with open(GRADES_FILE, 'r') as f:
        for line in f:
            sid, cid, marks, grade = line.strip().split(',')
            if cid == course_id:
                student_grades.append({'id': sid, 'marks': float(marks)})

    if not student_grades:
        print("No students have been graded for this course yet.")
        print("-" * 50)
        return

    marks_list = [g['marks'] for g in student_grades]
    average_marks = sum(marks_list) / len(marks_list)
    highest_marks = max(marks_list)
    lowest_marks = min(marks_list)

    print(f"Average Marks: {average_marks:.2f}%")
    print(f"Highest Marks: {highest_marks:.2f}%")
    print(f"Lowest Marks: {lowest_marks:.2f}%")
    print("\nEnrolled Students:")
    for grade_info in student_grades:
        print(f"  Student ID: {grade_info['id']}, Marks: {grade_info['marks']:.2f}%")
    print("-" * 50)


def export_performance_report():
    """Exports a performance report to a text file."""
    print("\n--- Export Performance Report ---")
    student_id = get_non_empty_input("Enter Student ID to export report: ")
    if not student_exists(student_id):
        print("Error: Student ID not found.")
        return

    filename = f"report_{student_id}.txt"
    try:
        with open(filename, 'w') as f:
            f.write(f"Performance Report for Student ID: {student_id}\n")
            f.write("-" * 50 + "\n")
            found_grades = False
            with open(GRADES_FILE, 'r') as grades_file:
                for line in grades_file:
                    sid, course_id, marks, grade = line.strip().split(',')
                    if sid == student_id:
                        f.write(f"Course: {course_id}, Marks: {float(marks):.2f}%, Grade: {grade}\n")
                        found_grades = True
            
            if not found_grades:
                f.write("No grades recorded for this student yet.\n")
            f.write("-" * 50 + "\n")
        print(f"Report successfully exported to {filename}")
    except IOError as e:
        print(f"Error exporting report: {e}")

def delete_student_grade():
    """Deletes a student's grade for a specific course."""
    print("\n--- Delete Student Grade ---")
    student_id = get_non_empty_input("Enter Student ID: ")
    if not student_exists(student_id):
        print("Error: Student ID not found.")
        return

    course_id = get_non_empty_input("Enter Course ID: ").upper()
    if not course_exists(course_id):
        print("Error: Course ID not found.")
        return

    try:
        with open(GRADES_FILE, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No grades recorded yet.")
        return

    record_deleted = False
    updated_lines = []
    for line in lines:
        sid, cid, _, _ = line.strip().split(',')
        if not (sid == student_id and cid.upper() == course_id):
            updated_lines.append(line)
        else:
            record_deleted = True

    if record_deleted:
        with open(GRADES_FILE, 'w') as f:
            f.writelines(updated_lines)
        print("Student grade deleted successfully!")
    else:
        print("Error: Grade record not found for the given Student ID and Course ID.")

def display_all_students():
    """Displays all student records."""
    print("\n--- Display All Student Records ---")
    print("-" * 50)
    try:
        with open(STUDENTS_FILE, 'r') as f:
            for line in f:
                student_id, name, email = line.strip().split(',')
                print(f"ID: {student_id}, Name: {name}, Email: {email}")
    except FileNotFoundError:
        print("No student records found.")
    print("-" * 50)

# -- Main Menu and Program Loop --

def main_menu():
    """Displays the main menu and returns the user's choice."""
    print("\n===== Python-Powered Student Grading System =====")
    print("1. Add New Student")
    print("2. Add New Course")
    print("3. Update Course")
    print("4. Delete Course")
    print("5. Record Student Marks")
    print("6. Display Individual Student Performance")
    print("7. Display Course Performance Summary")
    print("8. Export Performance Report")
    print("9. Delete Student Grade")
    print("10. Display All Students")
    print("11. Exit")
    print("=" * 51)
    
    choice = get_non_empty_input("Enter your choice (1-11): ")
    return choice

def main():
    """The main function to run the program."""
    initialize_files()
    
    while True:
        choice = main_menu()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            update_course()
        elif choice == '4':
            delete_course()
        elif choice == '5':
            record_student_marks()
        elif choice == '6':
            display_student_performance()
        elif choice == '7':
            display_course_performance()
        elif choice == '8':
            export_performance_report()
        elif choice == '9':
            delete_student_grade()
        elif choice == '10':
            display_all_students()
        elif choice == '11':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")
        
        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main()
