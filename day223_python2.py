from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Ravi"},
    {"id": 2, "name": "Priya"}
]

@app.route("/students")
def get_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True)
