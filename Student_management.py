import os

# Function to read all student data from the file
def read_students_from_file():
    students = []
    if os.path.exists("students.csv"):
        with open("students.csv", "r") as file:
            lines = file.readlines()
            for line in lines:
                student_data = line.strip().split(",")
                students.append({
                    "ID": student_data[0],
                    "Name": student_data[1],
                    "Partner": student_data[2],
            
                })
    return students

# Function to write student data to the file
def write_students_to_file(students):
    with open("students.csv", "w") as file:
        for student in students:
            student_info = f"{student['ID']},{student['Name']},{student['Partner']}\n"
            file.write(student_info)

# Function to add a new student record
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    partner = input("Enter Student Partner: ")

    students = read_students_from_file()
    students.append({
        "ID": student_id,
        "Name": name,
        "Partner": partner
    })
    write_students_to_file(students)
    print("Student added successfully!")

# Function to update an existing student record
def update_student():
    student_id = input("Enter Student ID to update: ")
    students = read_students_from_file()
    for student in students:
        if student["ID"] == student_id:
            print(f"Current details of Student ID {student_id}:")
            print(f"Name: {student['Name']}, Partner: {student['Partner']}")
            name = input("Enter new name (leave blank to keep current): ")
            partner = input("Enter new partner (leave blank to keep current): ")

            if name:
                student["Name"] = name
            if partner:
                student["Partner"] = partner

            write_students_to_file(students)
            print("Student details updated successfully!")
            return
    print("Student ID not found!")

# Function to delete a student record
def delete_student():
    student_id = input("Enter Student ID to delete: ")
    students = read_students_from_file()
    students = [student for student in students if student["ID"] != student_id]
    
    write_students_to_file(students)
    print(f"Student with ID {student_id} deleted successfully!")

# Function to display all students
def display_students():
    students = read_students_from_file()
    if students:
        print("Student Records:")
        for student in students:
            print(f"ID: {student['ID']}, Name: {student['Name']}, Partner: {student['Partner']}")
    else:
        print("No student records found.")

# Main function to interact with the system
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
