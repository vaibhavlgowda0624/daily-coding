students = [
    ("Ravi", 75),
    ("Priya", 92),
    ("Aman", 81),
    ("Kiran", 68)
]

students.sort(key=lambda student: student[1], reverse=True)

for student in students:
    print(student)
