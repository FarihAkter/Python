import sqlite3

class StudentDB:
    def __init__(self):
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT,
            dept TEXT
        )
        """)
        self.conn.commit()

    # CREATE
    def add_student(self, name, student_id, dept):
        self.cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?)",
            (student_id, name, dept)
        )
        self.conn.commit()
        print("Student added to database!")

    # READ
    def view_students(self):
        self.cursor.execute("SELECT * FROM students")
        data = self.cursor.fetchall()

        if not data:
            print("No students found!")
            return

        for i, s in enumerate(data, start=1):
            print(f"{i}. ID:{s[0]} | Name:{s[1]} | Dept:{s[2]}")

    # SEARCH
    def search_student(self, student_id):
        self.cursor.execute(
            "SELECT * FROM students WHERE id=?",
            (student_id,)
        )
        data = self.cursor.fetchone()

        if data:
            print("Found:", data)
        else:
            print("Student not found!")

    # UPDATE
    def update_student(self, student_id, name, dept):
        self.cursor.execute(
            "UPDATE students SET name=?, dept=? WHERE id=?",
            (name, dept, student_id)
        )
        self.conn.commit()
        print("Updated successfully!")

    # DELETE
    def delete_student(self, student_id):
        self.cursor.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )
        self.conn.commit()
        print("Deleted successfully!")