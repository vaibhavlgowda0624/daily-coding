import json

with open("student.json", "r") as file:
    student = json.load(file)

print("Student:", student["name"])
print("Course:", student["course"])
