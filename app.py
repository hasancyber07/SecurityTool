from flask import Flask, request, jsonify
import os

app = Flask(__name__)

API_KEY = "12345SECRET"

@app.route("/log", methods=["POST"])
def log_data():
    key = request.headers.get("x-api-key")

    if key != API_KEY:
        return jsonify({"error": "unauthorized"}), 403

    data = request.json

    with open("log.txt", "a") as f:
        f.write(str(data) + "\n")

    return jsonify({"status": "saved"})