from flask import Flask, jsonify, request
from stores import STORES
from geo import find_nearest_store

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/stores")
def list_stores():
    return jsonify({"stores": STORES})


@app.route("/nearest")
def nearest():
    address = request.args.get("address")
    if not address:
        return jsonify({"error": "address parameter required"}), 400
    
    nearest_store = find_nearest_store(address, STORES)
    return jsonify({"nearest": nearest_store})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
