# Student Management System in Python
A terminal program to manage student records (id, name, surname, grade) stored in a text file, supporting add, list, update delete and search operations.

---

## Features
- Add a new student with ID, name, surname and grade
- Delete a student record
- List all students
- Search student by name or surname
- Update existing student information
- Store data persistently in a `students.txt` file using file I/O

---

## Skills Demonstrated
- Python fundamentals (functions, loops, conditionals)
- File I/O (reading and writing text files)
- Data structures (list and dictionary)
- Error handling (try/except)
- Basic CRUD operations (Create, Read, Update, Delete)

---

## How to Run
1. Run the program:
```bash
python main.py
```
2. After running the program, you will see the following menu:
```markdown
=== STUDENT MANAGEMENT SYSTEM ===
1. Add Student
2. List Students
3. Delete Student
4. Update Student
5. Search Student
6. Exit
```
3. Enter the number corresponding to the desired action.

---

## Notes
The program creates `students.txt` automatically if it doesn't exist.

The student data is stored in `students.txt` is in the format:
```bash
id,name,surname,grade
```
