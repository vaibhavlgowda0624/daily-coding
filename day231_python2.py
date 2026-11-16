student1 = {
    "name": "Ravi",
    "marks": 80
}

student2 = {
    "course": "MCA",
    "semester": 3
}

combined = {**student1, **student2}

print(combined)
