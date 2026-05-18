from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Security Tool Online ✔"

@app.route("/log", methods=["POST"])
def log_data():
    data = request.json

    with open("log.txt", "a") as f:
        f.write(str(data) + "\n")

    return jsonify({"status": "saved"})

@app.route("/logs")
def get_logs():
    if not os.path.exists("log.txt"):
        return "No logs yet..."

    with open("log.txt", "r") as f:
        return f.read()

# ⚠️ Render üçün vacib
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)