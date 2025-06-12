import pickle
import pandas as pd

# Load the enhanced model (with ColumnTransformer inside)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_fraud(claim_amount, num_of_accidents, age, claim_type, region):
    # Construct DataFrame with expected column names
    input_df = pd.DataFrame([{
        "claim_amount": claim_amount,
        "num_of_accidents": num_of_accidents,
        "age": age,
        "claim_type": claim_type.lower(),
        "region": region.lower()
    }])

    # Predict
    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    return {
        "prediction": "Fraudulent" if prediction else "Legitimate",
        "confidence": round(prob * 100, 2)
    }
