# Presentation: Python-Powered Student Grading System

---

## Slide 1: Title Slide

**Python-Powered Student Grading System**

**Group Project for CSC1024 Programming Principles**

---

## Slide 2: Introduction

*   **What is it?** A command-line based application for managing student records, courses, and grades.
*   **Purpose:** To provide a simple, efficient, and "dummy-proof" system for educators.
*   **Technology:** Built entirely with standard Python 3, requiring no external libraries.
*   **Target User:** Educators or administrators who need a straightforward tool for grade management.

---

## Slide 3: System Design & Architecture

*   **Interface:** A simple and intuitive Command-Line Interface (CLI).
*   **Paradigm:** Developed using a procedural programming approach, organizing code into logical functions.
*   **Portability:** Runs on any system with Python 3 installed. No external dependencies needed.
*   **Data Storage:** Persists data in simple, human-readable comma-separated text files (`.txt`).

---

## Slide 4: Core Features

The system offers a comprehensive set of features through a menu-driven interface:

1.  **Add New Student:** Create new student records.
2.  **Add New Course:** Add new courses to the system.
3.  **Update Course:** Modify the name of an existing course.
4.  **Delete Course:** Remove a course and all its associated grades.
5.  **Record Student Marks:** Enter or update marks for a student in a course.
6.  **Display Individual Student Performance:** View a report for a single student.
7.  **Display Course Performance Summary:** See average, highest, and lowest marks for a course.
8.  **Export Performance Report:** Save a student's performance report to a text file.
9.  **Delete Student Grade:** Remove a specific grade entry for a student.
10. **Display All Students:** View a list of all students in the system.
11. **Exit:** Close the application.

---

## Slide 5: Data Management

*   **Method:** Plain text files (`students.txt`, `courses.txt`, `grades.txt`) act as the database.
*   **Format:** A simple and robust Comma-Separated Values (CSV) like structure:
    *   `students.txt`: `student_id,name,email`
    *   `courses.txt`: `course_id,course_name`
    *   `grades.txt`: `student_id,course_id,marks,grade`
*   **Initialization:** The `initialize_files()` function automatically creates these files if they don't exist, preventing runtime errors.

---

## Slide 6: Code Structure

The `main.py` script is logically divided for clarity and maintainability:

*   **Constants:** Global constants for file paths.
*   **Helper Functions:** Reusable functions for common tasks like input validation (`get_non_empty_input`, `is_valid_email`) and grade calculation.
*   **Core Feature Functions:** Each menu option corresponds to a dedicated function (e.g., `add_student()`, `delete_course()`).
*   **Main Program Loop:** The `main()` function drives the application, displaying the menu and calling the appropriate functions.

---

## Slide 7: Error Handling & Robustness

The system is designed to be "dummy-proof":

*   **Input Validation:**
    *   Prevents empty inputs.
    *   Ensures numeric inputs are valid numbers within the 0-100 range.
    *   Validates email and course name formats using regular expressions.
*   **Data Integrity:**
    *   Checks for duplicate Student and Course IDs to prevent data corruption.
    *   Warns the user before deleting a course with associated grades.
*   **File Safety:** Proactively creates data files to avoid `FileNotFoundError`.

---

## Slide 8: Live Demonstration

*(This slide is a placeholder for a live demonstration of the running application, showcasing the features in action.)*

**Demo Plan:**

1.  Start the application.
2.  Add a new student and a new course.
3.  Record marks for the student in that course.
4.  Display the student's performance report.
5.  Show the course performance summary.
6.  Export the student's report to a file.
7.  Demonstrate an error case (e.g., entering invalid input).

---

## Slide 9: Conclusion

*   **A Functional System:** The project successfully delivers a functional and robust student grading system.
*   **Simplicity and Portability:** By using only standard Python, the application is easy to run and maintain.
*   **User-Centric Design:** The menu-driven interface and comprehensive error handling create a positive user experience.
*   **Future Enhancements:** Could be extended with features like batch imports, more complex analytics, or a graphical user interface (GUI).

---

## Slide 10: Q&A

**Thank you!**

**Any questions?**
