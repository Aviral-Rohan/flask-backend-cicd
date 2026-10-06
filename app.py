import os
from datetime import datetime, timezone

from flask import Flask, jsonify, request

app = Flask(__name__)

# The port comes from the environment, so the same code runs anywhere
PORT = int(os.getenv("PORT", "5000"))


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "flask-backend"})


@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json(silent=True) or request.form
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()

    if not name or not email:
        return jsonify({"error": "Name and Email are both required."}), 400

    record = {
        "name": name,
        "email": email,
        "received_at": datetime.now(timezone.utc).isoformat(),
    }
    return jsonify({"message": f"Hello {name}, your data was received by the Flask backend!",
                    "data": record}), 201


if __name__ == "__main__":
    # 0.0.0.0 = listen on all network interfaces
    app.run(host="0.0.0.0", port=PORT)
