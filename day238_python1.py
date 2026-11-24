from flask import Flask, request, jsonify

app = Flask(__name__)

students = []
next_id = 1

@app.route("/students", methods=["POST"])
def create_student():
    global next_id

    data = request.get_json(silent=True) or {}

    if not data.get("name"):
        return jsonify({"error": "Name required"}), 400

    student = {
        "id": next_id,
        "name": data["name"]
    }

    students.append(student)
    next_id += 1

    return jsonify(student), 201

if __name__ == "__main__":
    app.run(debug=True)
