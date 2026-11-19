import sqlite3

connection = sqlite3.connect("university.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    duration INTEGER
)
""")

connection.commit()
connection.close()

print("Courses table created")
