from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True) or {}

    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    return jsonify({
        "message": "Student received",
        "student": data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
