from flask import Flask, request, jsonify
import random
from string import ascii_lowercase
from flask_cors import CORS

import dataset as datasetConverter
import dissertation as dissertationConverter
import refUpdate as refUpdateConverter


app = Flask(__name__)
CORS(app)


@app.route("/upload", methods=["POST"])
def upload():
    fileID = f"{''.join(random.choice(ascii_lowercase) for i in range(10))}"

    csvfile = request.files['file']
    destination = f"./temp/{fileID}"
    csvfile.save(destination)

    response = jsonify({"fileID": fileID})
    return response


@app.route("/dissertation", methods=["POST"])
def dissertation():
    batchID = request.json["batchid"]
    depname = request.json["depname"]
    depemail = request.json["depemail"]
    registrant = request.json["registrant"]

    fileID = request.json["fileID"]

    xml = dissertationConverter.go(
        batchID, depname, depemail, registrant, fileID)

    response = jsonify(
        {"response": xml})
    return response


@app.route("/dataset", methods=["POST"])
def dataset():
    batchID = request.json["batchid"]
    depname = request.json["depname"]
    depemail = request.json["depemail"]
    registrant = request.json["registrant"]
    dbname = request.json["dbname"]

    fileID = request.json["fileID"]

    xml = datasetConverter.go(
        batchID, depname, depemail, registrant, dbname, fileID)

    response = jsonify(
        {"response": xml})
    return response


@app.route("/refUpdate", methods=["POST"])
def refUpdate():
    batchID = request.json["batchid"]
    depname = request.json["depname"]
    depemail = request.json["depemail"]

    fileID = request.json["fileID"]

    xml = refUpdateConverter.go(
        batchID, depname, depemail, fileID)

    response = jsonify(
        {"response": xml})
    return response


if __name__ == "__main__":
    app.run(debug=True, port=443, host="0.0.0.0")
