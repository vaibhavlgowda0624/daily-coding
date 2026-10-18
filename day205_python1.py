import sqlite3

with sqlite3.connect("college.db") as connection:
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (name, course) VALUES (?, ?)",
        ("Asha", "MCA")
    )

    cursor.execute("SELECT id, name, course FROM students")

    for student in cursor.fetchall():
        print(student)
