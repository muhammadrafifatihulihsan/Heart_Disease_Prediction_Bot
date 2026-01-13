import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "knn_model.pkl"
SCALER_PATH = BASE_DIR / "scaler.pkl"

print("Model path:", MODEL_PATH)
print("Scaler path:", SCALER_PATH)

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

FEATURES = [
    "Age",
    "Sex",
    "Chest pain type",
    "BP",
    "Cholesterol",
    "FBS over 120",
    "EKG results",
    "Max HR",
    "Exercise angina",
    "ST depression",
    "Slope of ST",
    "Number of vessels fluro",
    "Thallium",
]

def predict(data: dict) -> str:
    df = pd.DataFrame([data], columns=FEATURES)
    scaled = scaler.transform(df)
    result = model.predict(scaled)[0]
    return "Presence" if result == 1 else "Absence"
