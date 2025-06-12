# app/train_model.py
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

# Sample dataset (fake claims data)
data = {
    "claim_amount": [1000, 2000, 30000, 5000, 45000, 700],
    "num_of_accidents": [0, 1, 5, 0, 6, 0],
    "is_fraud": [0, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

X = df.drop("is_fraud", axis=1)
y = df["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression()
model.fit(X_train, y_train)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")

