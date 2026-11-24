from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Ravi"},
    {"id": 2, "name": "Priya"}
]

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
