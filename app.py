from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

API_KEY = "SECURE123"

# HTML UI BURDA SERVE OLUNUR
@app.route("/")
def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route("/log", methods=["POST"])
def log_data():
    key = request.headers.get("x-api-key")

    if key != API_KEY:
        return jsonify({"error": "unauthorized"}), 403

    data = request.json

    with open("log.txt", "a") as f:
        f.write(str(data) + "\n")

    return jsonify({"status": "saved"})

@app.route("/logs")
def get_logs():
    if not os.path.exists("log.txt"):
        return ""

    with open("log.txt", "r") as f:
        return f.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)