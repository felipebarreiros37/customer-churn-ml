from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_churn
from datetime import datetime
import logging


# Configuração de logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("churn-monitor")


app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn using XGBoost.",
    version="1.0.0"
)


class Customer(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API",
        "status": "running"
    }


@app.post("/predict")
def predict(customer: Customer):

    customer_data = customer.model_dump()

    result = predict_churn(customer_data)

    # Monitoring
    logger.info(
        "prediction_time=%s prediction=%s probability=%.4f tenure=%s monthly_charges=%.2f",
        datetime.now().isoformat(),
        result["prediction_label"],
        result["churn_probability"],
        customer.tenure,
        customer.MonthlyCharges
    )

    return result