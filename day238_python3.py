from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Ravi"},
    {"id": 2, "name": "Priya"}
]

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json(silent=True) or {}

    for student in students:
        if student["id"] == student_id:
            if not data.get("name"):
                return jsonify({"error": "Name required"}), 400

            student["name"] = data["name"]
            return jsonify(student)

    return jsonify({"error": "Not found"}), 404


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return jsonify({"message": "Deleted"})

    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
