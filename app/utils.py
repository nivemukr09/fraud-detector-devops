# app/utils.py
import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_fraud(claim_amount, num_of_accidents):
    features = np.array([[claim_amount, num_of_accidents]])
    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0][1]
    return {"is_fraud": bool(prediction), "confidence": round(prob, 2)}

