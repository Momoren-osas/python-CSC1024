# Gemini Project Context: Python Student Grading System

## Project Overview

This project is a command-line based **Student Grading System** written in Python. Its purpose is to manage student records, course information, and grades based on the requirements specified in the `CSC1024 Programming Principles-Final Project.pdf` document.

The application is built as a single-script solution (`main.py`) and uses Python's standard library exclusively, meaning it has no external dependencies. Data persistence is handled through simple comma-separated text files (`.txt`).

## Building and Running

### Prerequisites
- Python 3.x

### Running the Application
The application can be run directly from the command line:
```bash
python main.py
```
Upon starting, the script will create the necessary data files (`students.txt`, `courses.txt`, `grades.txt`) if they do not already exist.

### Testing
There are no automated test suites for this project. Testing should be performed manually by running the application and verifying the functionality of its various menu options.

## Development Conventions

### Code Style
The code adheres to standard Python conventions, using `snake_case` for function and variable names. It is organized into three main sections: helper functions, core functionality for each menu option, and a main loop that drives the user interface.

### Data Storage
The application uses the following text files for data persistence:
- **`students.txt`**: Stores student information.
  - Format: `student_id,name,email`
- **`courses.txt`**: Stores course information.
  - Format: `course_id,course_name`
- **`grades.txt`**: Stores grade records for students.
  - Format: `student_id,course_id,marks,grade`
- **`report_*.txt`**: Performance reports are exported to files with this naming convention.

### Error Handling
The application is designed to be "dummy-proof" by validating user input at every step. This prevents common errors such as empty inputs, non-numeric values where numbers are expected, and invalid email formats.

## Code Explanations

### `import os` and `initialize_files()`

*   **`import os`**:
    *   **Purpose**: This line imports Python's built-in `os` module. The `os` module provides a way of using operating system dependent functionality. This includes interacting with the file system, handling paths, and other system-related tasks.
    *   **In this context**: It is specifically used here for checking the existence of files and creating new files, which are file system operations.

*   **`initialize_files()` function**:
    *   **Purpose**: The primary goal of this function is to ensure that the data files required by the grading system (`students.txt`, `courses.txt`, `grades.txt`) exist before the program attempts to read from or write to them. This prevents `FileNotFoundError` exceptions when the application starts for the first time or if these files are accidentally deleted.
    *   **Mechanism**:
        *   It defines a list of `filename` constants (`STUDENTS_FILE`, `COURSES_FILE`, `GRADES_FILE`).
        *   It then iterates through each `filename` in this list.
        *   For each `filename`, `os.path.exists(filename)` is called. This function from the `os.path` submodule checks if a file or directory at the specified path exists.
        *   If `os.path.exists(filename)` returns `False` (meaning the file does not exist), the code block `with open(filename, 'w') as f: pass` is executed:
            *   `open(filename, 'w')`: This attempts to open the specified `filename` in 'write' mode (`'w'`). If the file does not exist, Python automatically creates it. If it does exist, its content would be truncated (emptied), but in this specific `initialize_files` context, it only runs if the file *doesn't* exist.
            *   `as f:`: Assigns the opened file object to the variable `f`.
            *   `pass`: This is a null operation. It means "do nothing" inside the `with` block. The mere act of opening the file in 'w' mode is sufficient to create it; no content needs to be written initially.
        *   The `with` statement ensures that the file is properly closed automatically, even if errors occur.
    *   **In essence**: This function acts as a setup routine to make sure the application has the necessary empty files to work with, avoiding runtime errors related to missing data files.