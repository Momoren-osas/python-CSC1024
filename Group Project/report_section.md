## System Design and Architecture

### 1. Introduction & Overall Architecture

The student grading system is designed as a console-based application, providing users with a Command-Line Interface (CLI) for all interactions. The architecture is intentionally straightforward, implemented as a single Python script (`main.py`).

A key design decision was to develop the application using a procedural programming paradigm. This approach organizes the code around procedures or functions that perform specific tasks, which aligns well with the menu-driven nature of the system. Furthermore, the project relies exclusively on Python's built-in standard libraries, such as `os` for file system interaction and `re` for regular expression-based email validation. This self-imposed constraint ensures maximum portability and simplicity, as the application can run on any system with a standard Python 3 installation without requiring any external package installations.

### 2. Code Structure & Modularity

Despite being a single-file application, `main.py` is logically segmented to enhance readability and maintainability. The code is organized into four main areas:

*   **Constants:** Defined at the beginning of the script, global constants (`STUDENTS_FILE`, `COURSES_FILE`, `GRADES_FILE`) centralize critical file paths, making them easy to locate and modify.
*   **Helper Functions:** A collection of small, focused utility functions that encapsulate common operations such as input validation (`get_non_empty_input`, `get_numeric_input`), specific data format validation (`is_valid_email`), and core logic components (`calculate_grade`, `student_exists`, `course_exists`). These functions promote code reusability and simplify the main feature implementations.
*   **Core Feature Functions:** Each major functionality of the grading system, such as `add_student()`, `add_course()`, `update_course()`, `delete_course()`, `record_student_marks()`, `delete_student_grade()`, `display_student_performance()`, `display_course_performance()`, and `export_performance_report()`, is implemented as a standalone function. This modular approach ensures that each feature is self-contained, improving clarity and making it easier to debug or extend individual components. Notably, `delete_course()` includes checks for associated grades to prevent orphaned data.
*   **Main Program Loop (`main()` function):** This function serves as the application's orchestrator. It initializes the necessary data files and then enters a continuous loop that displays the main menu, captures user input, and dispatches control to the appropriate core feature function based on the user's selection. This clear separation of concerns helps manage the overall application flow.

### 3. Data Persistence & Management

To ensure data persists between application runs, the system employs a simple yet effective file-based storage mechanism.

*   **Storage Method:** The design choice was to use plain text files (`.txt`) as the database. This method avoids the complexity of a full-fledged database system and keeps the application lightweight and portable, in line with the project's requirements.

*   **File Format:** Data is stored in a structured, line-by-line format, with each field separated by a comma. This mimics a standard Comma-Separated Values (CSV) structure, which is both human-readable and easy to parse programmatically. The three data files are:
    *   `students.txt`: Stores student records (`student_id,name,email`).
    *   `courses.txt`: Stores course information (`course_id,course_name`).
    *   `grades.txt`: Stores grading records, linking students and courses (`student_id,course_id,marks,grade`).

*   **Data Initialization:** A critical feature of the data management design is the `initialize_files()` function. This function is executed once at application startup. It checks for the existence of the required data files and creates them if they are missing. This preventative measure ensures the application does not crash due to a `FileNotFoundError` on its first launch or if the files are accidentally deleted.

### 4. User Interaction & Program Flow

The application's interaction model is centered around a menu-driven Command-Line Interface (CLI), ensuring a predictable and guided user experience.

*   **Main Menu Loop:** The core of the program's execution resides within the `main()` function's `while True:` loop. This loop continuously displays the main menu options to the user, providing a clear overview of available functionalities, now expanded to include operations like updating/deleting courses and deleting student grades.

*   **User Input and Dispatch:** After presenting the menu, the program prompts the user to enter a choice (e.g., from 1-11). This input is then processed through a series of `if/elif/else` conditional statements. Each valid choice directly invokes the corresponding core feature function (e.g., entering '1' calls `add_student()`, '4' calls `delete_course()`). This direct mapping ensures that user selections are immediately translated into specific actions.

*   **Sequential Interaction:** Following the completion of each selected task, the user is prompted to "Press Enter to return to the main menu...". This mechanism provides a simple, explicit control flow, ensuring users are always aware of how to navigate back to the main options and prevents them from getting lost within sub-processes. This sequential interaction pattern reinforces the guided nature of the CLI.

### 5. Error Handling & Robustness

A core principle in the system's design is to create a "dummy-proof" application that can gracefully handle various user inputs and prevent common errors.

*   **Comprehensive Input Validation:** The system implements robust validation checks at every point where user input is required:
    *   **Non-empty Input:** Functions like `get_non_empty_input()` ensure that users cannot proceed with empty fields, prompting them to re-enter data until valid input is provided.
    *   **Numeric Range and Type Validation:** For numerical inputs, such as student marks, `get_numeric_input()` verifies that the input is indeed a number and falls within acceptable ranges (e.g., 0-100). It handles `ValueError` exceptions for non-numeric entries.
    *   **Format Validation:** The `is_valid_email()` function utilizes regular expressions to enforce a standard email format, guiding users to correct invalid entries. Additionally, `is_valid_course_name()` ensures that course names consist only of alphabetic characters and spaces, preventing invalid course designations.
    *   **Grade Formatting and Precision:** Numeric inputs for marks are now automatically rounded to two decimal places and displayed with a percentage symbol, improving data consistency and user readability across all performance reports.

*   **Data Integrity Checks:** Before adding new records, the system checks for potential data conflicts:
    *   **Duplicate IDs:** Functions like `student_exists()` and `course_exists()` prevent the creation of duplicate student or course IDs, ensuring that each record is unique and maintaining data consistency within the text files.

*   **File Handling Safety:** The `initialize_files()` function, as described in the Data Persistence section, plays a crucial role in robustness by proactively creating necessary data files. This eliminates `FileNotFoundError` as a potential failure point during normal operation.

