

# Student Management System

## Overview

The **Student Management System** is a Python-based program designed to store and manage student records. It provides a simple, user-friendly interface to allow users to add, update, delete, and view student details, with all data being persistently stored through file handling. This system can be used in educational institutions to maintain student records or in any scenario where managing student data is required.

## Features

- **Add Student**: Add new student records including their name, ID, grade, etc.
- **View Student**: Display student information.
- **Update Student**: Modify existing student records.
- **Delete Student**: Remove student records from the system.
- **Persistent Storage**: All student records are saved in a file, ensuring the data is retained across sessions.
  
## Technologies Used

- Python
- File Handling (for persistent storage)

## Prerequisites

Before running the program, make sure you have the following installed:

- Python 3.x
- Text editor or IDE (e.g., VSCode, PyCharm, etc.)


## Usage

1. Run the `main.py` file:

```bash
python main.py
```

2. The program will display a menu with the following options:
   - **1**: Add Student
   - **2**: View Student
   - **3**: Update Student
   - **4**: Delete Student
   - **5**: Exit

3. Enter the corresponding number for the operation you want to perform.

4. The system will prompt you for the necessary information (e.g., student name, ID, etc.) depending on the operation.

## File Structure

```
student-management-system/
│
├── main.py           # Main program file
├── students.txt      # File to store student records
└── README.md         # Project documentation (this file)
```

### students.txt

The `students.txt` file is where all student data is stored. Each record is saved in a structured format that the program can read and modify.

## Example

Here’s an example of adding a student:

```
Enter student ID: 123
Enter student name: John Doe
Enter student grade: A
Student added successfully!
```

Upon viewing the students, you might see:

```
Student ID: 123
Name: John Doe
Grade: A
```
