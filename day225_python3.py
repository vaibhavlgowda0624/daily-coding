import json

with open("student.json", "r") as file:
    student = json.load(file)

student["semester"] = 3

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Student information updated.")
