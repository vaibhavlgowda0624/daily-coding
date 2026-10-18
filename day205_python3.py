import sqlite3

name = input("Enter student name to search: ").strip()

with sqlite3.connect("college.db") as connection:
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, course FROM students WHERE name = ?",
        (name,)
    )

    results = cursor.fetchall()

    if results:
        for student in results:
            print(student)
    else:
        print("No matching student found.")
