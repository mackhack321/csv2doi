from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/greeter", methods=["POST"])
def greetme():
    name = request.json["name"]
    age = request.json["age"]
    response = jsonify(
        {"response": f"Hello, {name}! It's cool that you're {age} years old."})

    return response


if __name__ == "__main__":
    app.run(debug=True)
