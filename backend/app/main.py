# app/main.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import predict_fraud

app = Flask(__name__)
CORS(app)

@app.route("/")
def health():
    return "Insurance Claim Fraud Detector is up!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    claim_amount = data.get("claim_amount")
    num_of_accidents = data.get("num_of_accidents")
    age = data.get("age")
    claim_type = data.get("claim_type")
    region = data.get("region")

    if None in (claim_amount, num_of_accidents, age, claim_type, region):
        return jsonify({"error": "Missing fields"}), 400

    result = predict_fraud(claim_amount, num_of_accidents, age, claim_type, region)
    return jsonify(result)

# Correct position and indentation
if __name__ == "__main__":
    app.run(debug=True)
