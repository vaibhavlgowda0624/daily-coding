import sqlite3

courses = [
    ("Python", 3),
    ("Java", 4),
    ("Cybersecurity", 6)
]

with sqlite3.connect("university.db") as connection:
    connection.executemany(
        "INSERT INTO courses (name, duration) VALUES (?, ?)",
        courses
    )

print("Courses inserted")
