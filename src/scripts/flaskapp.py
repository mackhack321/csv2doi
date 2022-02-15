from flask import Flask, request, jsonify
import random
from string import ascii_lowercase
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/upload", methods=["POST"])
def upload():
    fileID = f"{''.join(random.choice(ascii_lowercase) for i in range(10))}"

    csvfile = request.files['file']
    destination = f"./uploads/{fileID}.py"
    csvfile.save(destination)

    response = jsonify({"fileID": fileID})
    return response


@app.route("/dissertation")
def dissertation():
    batchID = request.json["batchid"]
    depname = request.json["depname"]
    depemail = request.json["depemail"]
    registrant = request.json["registrant"]
    fileID = request.json["fileID"]

    # makes filename that looks like "[depositor name] [5 random lowercase letters].xml"
    filename = f"{depname} {''.join(random.choice(ascii_lowercase) for i in range(5))}.xml"

    return jsonify(filename=filename)


@app.route("/dataset", methods=["POST"])
def dataset():
    batchID = request.json["batchid"]
    depname = request.json["depname"]
    depemail = request.json["depemail"]
    registrant = request.json["registrant"]
    dbname = request.json["dbname"]

    fileID = request.json["fileID"]

    # makes filename that looks like "[depositor name] [5 random lowercase letters].xml"
    response = jsonify(
        {"response": f"roger wilco. heard you with file ID {fileID}"})
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5003, host="0.0.0.0")
