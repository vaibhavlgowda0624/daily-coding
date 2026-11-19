import sqlite3

duration = 4

with sqlite3.connect("university.db") as connection:
    results = connection.execute(
        "SELECT * FROM courses WHERE duration >= ?",
        (duration,)
    ).fetchall()

for course in results:
    print(course)
