students = [
    {"name": "Ravi", "marks": 85},
    {"name": "Priya", "marks": 92}
]

html = "<table border='1'>"

for student in students:
    html += (
        f"<tr><td>{student['name']}</td>"
        f"<td>{student['marks']}</td></tr>"
    )

html += "</table>"

with open("students.html", "w") as file:
    file.write(html)

print("HTML report generated")
