students = [
    ("Ravi", "A"),
    ("Priya", "B"),
    ("Aman", "A"),
    ("Kiran", "C"),
    ("Neha", "B")
]

grades = {}

for name, grade in students:
    grades.setdefault(grade, []).append(name)

for grade, names in grades.items():
    print(grade, ":", names)
