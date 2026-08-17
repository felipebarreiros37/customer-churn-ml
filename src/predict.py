import joblib
import pandas as pd
from pathlib import Path


# Caminho raiz do projeto
PROJECT_ROOT = Path(__file__).resolve().parents[1]

MODEL_PATH = PROJECT_ROOT / "models" / "churn_model.joblib"
THRESHOLD_PATH = PROJECT_ROOT / "models" / "churn_threshold.joblib"


# Carrega os artefatos
model = joblib.load(MODEL_PATH)
threshold = joblib.load(THRESHOLD_PATH)


def predict_churn(customer_data):
    """
    Recebe os dados de um cliente e retorna
    probabilidade e classificação de churn.
    """

    customer_df = pd.DataFrame([customer_data])

    probability = model.predict_proba(
        customer_df
    )[:, 1][0]

    prediction = int(
        probability >= threshold
    )

    label = (
        "Churn"
        if prediction == 1
        else "No Churn"
    )

    return {
        "churn_probability": float(probability),
        "threshold": float(threshold),
        "prediction": prediction,
        "prediction_label": label
    }