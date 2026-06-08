from student_db import StudentDB

db = StudentDB()

def menu():
    print("\n===== STUDENT DB SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        sid = input("ID: ")
        dept = input("Dept: ")
        db.add_student(name, sid, dept)

    elif choice == "2":
        db.view_students()

    elif choice == "3":
        sid = input("Enter ID: ")
        db.search_student(sid)

    elif choice == "4":
        sid = input("ID: ")
        name = input("New name: ")
        dept = input("New dept: ")
        db.update_student(sid, name, dept)

    elif choice == "5":
        sid = input("ID: ")
        db.delete_student(sid)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")