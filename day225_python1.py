import json

student = {
    "id": 101,
    "name": "Vaibhav",
    "course": "MCA"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created.")
