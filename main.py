import json

students = []

def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except:
        students = []

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file)

def show_menu():
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

# CREATE
def add_student():
    name = input("Enter name: ")
    student_id = input("Enter ID: ")
    dept = input("Enter department: ")

    students.append({
        "name": name,
        "id": student_id,
        "dept": dept
    })

    save_data()
    print("Student added successfully!")

# READ
def view_students():
    if not students:
        print("No students found!")
        return

    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']} | {s['id']} | {s['dept']}")

# SEARCH
def search_student():
    key = input("Enter name or ID to search: ")

    found = False
    for s in students:
        if s["name"] == key or s["id"] == key:
            print("Found:", s)
            found = True

    if not found:
        print("Student not found!")

# UPDATE
def update_student():
    student_id = input("Enter ID to update: ")

    for s in students:
        if s["id"] == student_id:
            print("Current data:", s)

            s["name"] = input("New name: ")
            s["dept"] = input("New department: ")

            save_data()
            print("Updated successfully!")
            return

    print("Student not found!")

# DELETE
def delete_student():
    student_id = input("Enter ID to delete: ")

    for i, s in enumerate(students):
        if s["id"] == student_id:
            students.pop(i)
            save_data()
            print("Deleted successfully!")
            return

    print("Student not found!")

def main():
    load_data()

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()