# app/main.py
from flask import Flask, request, jsonify
from utils import predict_fraud

app = Flask(__name__)

@app.route("/")
def health():
    return "Insurance Claim Fraud Detector is up!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    claim_amount = data.get("claim_amount")
    num_of_accidents = data.get("num_of_accidents")

    if claim_amount is None or num_of_accidents is None:
        return jsonify({"error": "Missing fields"}), 400

    result = predict_fraud(claim_amount, num_of_accidents)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

