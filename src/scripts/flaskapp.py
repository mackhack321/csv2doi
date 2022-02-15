from flask import Flask, request, jsonify
import random
from string import ascii_lowercase
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/dissertation")
def dissertation():
    batchID = request.json["batchid"]
    depname = request.json["depname"]
    depemail = request.json["depemail"]
    registrant = request.json["registrant"]

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

    # makes filename that looks like "[depositor name] [5 random lowercase letters].xml"
    filename = f"{depname} {''.join(random.choice(ascii_lowercase) for i in range(5))}.xml"
    response = jsonify({"filename": filename})
    
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5003, host="0.0.0.0")
