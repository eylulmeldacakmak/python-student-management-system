def load_students():
    students = []
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line: #ignore if there is an empty line (wrong format)
                    continue
                parts = line.split(",")
                if len(parts) != 4: #ignore if the line doesn't have 4 parts (wrong format)
                    continue
                student_id, name, surname, grade = parts
                try:
                    student = {"id": int(student_id), "name": name, "surname": surname, "grade": int(grade)}
                except ValueError:
                    continue
                students.append(student)
    except FileNotFoundError:
        return [] #return an empty list if the file isn't available
    return students

def save_students(students):
    with open("students.txt", "w") as file:
        for student in students:
            line = f"{student['id']},{student['name']},{student['surname']},{student['grade']}\n"
            file.write(line)

def get_new_id(students):
    if not students:
        return 1
    return max(student["id"] for student in students) + 1 #so that we will not assign same IDs when we delete a student

def add_student():
    students = load_students()
    new_id = get_new_id(students)
    name = input("Name: ")
    surname = input("Surname: ")
    while True:
        try:
            grade = int(input("Grade: "))
            break
        except ValueError:
            print("Please enter a valid number for grade.")
    student = {"id" : new_id, "name" : name, "surname" : surname, "grade" : grade}

    students.append(student)
    save_students(students)
    print("Student added successfully.")

def delete_student():
    students = load_students()
    while True:
        try:
            student_id = int(input("Enter student ID to delete: "))
            break
        except ValueError:
            print("Please enter a valid number for ID.")
    new_list = [student for student in students if student["id"] != student_id]
    if len(new_list) == len(students):
        print("Student not found.")
    else:
        save_students(new_list)
        print("Student deleted successfully.")

def list_students():
    students = load_students()
    for student in students:
        print(f"{student['id']} - {student['name']} {student['surname']} - Grade: {student['grade']}")

def update_student():
    students = load_students()
    while True:
        try:
            student_id = int(input("Enter student ID to update: "))
            break
        except ValueError:
            print("Please enter a valid number for ID.")
    found = False
    for student in students:
        if student["id"] == student_id:
            found = True
            student["name"] = input("New name: ")
            student["surname"] = input("New surname: ")
            while True:
                try:
                    student_id = int(input("Enter student ID to update: "))
                    break
                except ValueError:
                    print("Please enter a valid number for ID.")
    if not found:
        print("Student not found.")
    else:
        save_students(students)
        print("Student updated.")

def search_student():
    students = load_students()
    keyword = input("Enter name or surname to search: ").lower()
    results = [student for student in students if keyword in student["name"].lower() or keyword in student["surname"].lower()]
    if not results:
        print("No students found.")
        return
    for s in results:
        print(f"{s['id']} - {s['name']} {s['surname']} - Grade: {s['grade']}")

def menu():
    while True:
        print("")
        print("=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. List Students")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Search Student")
        print("6. Exit")
        choice = input("Please enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

menu()