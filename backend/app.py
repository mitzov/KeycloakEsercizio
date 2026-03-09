from flask import Flask, request, jsonify
from flask_cors import CORS
from db import DatabaseWrapper

app = Flask(__name__)
CORS(app)


@app.route("/voti", methods=["GET"])
def voti():
    return jsonify(db.get_voti())


@app.route("/voti/<studente>", methods=["GET"])
def voti_studente(studente):
    return jsonify(db.get_voti_studente(studente))


@app.route("/voti", methods=["POST"])
def inserisci():

    data = request.json

    db.inserisci_voto(
        data["studente"],
        data["materia"],
        data["voto"]
    )

    return {"message": "voto inserito"}
    

if __name__ == "__main__":
    app.run(debug=True)