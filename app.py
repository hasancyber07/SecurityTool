from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)

API_KEY = "SECURE123"

@app.route("/")
def home():
    return "Security Tool PRO Online ✔"

@app.route("/log", methods=["POST"])
def log_data():
    key = request.headers.get("x-api-key")

    if key != API_KEY:
        return jsonify({"error": "unauthorized"}), 403

    data = request.json

    with open("log.txt", "a") as f:
        f.write(f"{time.ctime()} | {data}\n")

    return jsonify({"status": "saved"})

@app.route("/logs")
def get_logs():
    if not os.path.exists("log.txt"):
        return "No logs yet..."

    with open("log.txt", "r") as f:
        return f.read()

@app.route("/clear", methods=["POST"])
def clear_logs():
    key = request.headers.get("x-api-key")
    if key != API_KEY:
        return jsonify({"error": "unauthorized"}), 403

    open("log.txt", "w").close()
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)