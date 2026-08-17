# \# Customer Churn Prediction — End-to-End Machine Learning

# 

# End-to-end Machine Learning project for predicting customer churn, covering the entire workflow from data analysis and model training to deployment and monitoring in production.

# 

# \## Objective

# 

# Predict the probability of customer churn and identify customers with a higher risk of leaving the company.

# 

# \## Architecture

# 

# Data  

# ↓  

# Exploratory Data Analysis  

# ↓  

# Data Preprocessing  

# ↓  

# Feature Engineering  

# ↓  

# Machine Learning Pipeline  

# ↓  

# Model Training and Comparison  

# ↓  

# XGBoost  

# ↓  

# Model Serialization  

# ↓  

# FastAPI  

# ↓  

# Docker  

# ↓  

# Cloud Deployment  

# ↓  

# Monitoring

# 

# \## Technologies

# 

# \- Python

# \- Pandas

# \- Scikit-learn

# \- XGBoost

# \- FastAPI

# \- Pytest

# \- MLflow

# \- Docker

# \- Git

# \- GitHub

# \- Render

# 

# \## Project Structure

# 

# ```text

# customer-churn-ml/

# │

# ├── api/

# │   └── main.py

# │

# ├── models/

# │

# ├── src/

# │   ├── predict.py

# │   └── 02\_modeling.ipynb

# │

# ├── tests/

# │   └── test\_predict.py

# │

# ├── results/

# │

# ├── Dockerfile

# ├── docker-compose.yml

# ├── requirements.txt

# ├── pytest.ini

# └── README.md

# ```

# 

# \## Machine Learning Pipeline

# 

# The project uses a Machine Learning pipeline to ensure that the same data transformations are applied during both training and inference.

# 

# The workflow includes:

# 

# 1\. Data preparation

# 2\. Data preprocessing

# 3\. Feature engineering

# 4\. Model training

# 5\. Model comparison

# 6\. Model selection

# 7\. Model serialization

# 8\. Inference on new customer data

# 

# \## Prediction API

# 

# The trained model is exposed through a REST API built with FastAPI.

# 

# Main endpoint:

# 

# ```text

# POST /predict

# ```

# 

# The API receives customer information and returns:

# 

# \- Churn probability

# \- Classification threshold

# \- Prediction

# \- Prediction label

# 

# Example response:

# 

# ```json

# {

# &#x20; "churn\_probability": 0.7827,

# &#x20; "threshold": 0.33,

# &#x20; "prediction": 1,

# &#x20; "prediction\_label": "Churn"

# }

# ```

# 

# \## Automated Testing

# 

# Automated tests were implemented using Pytest.

# 

# Run the tests with:

# 

# ```bash

# pytest -v

# ```

# 

# The tests validate predictions for customers with different churn risk profiles.

# 

# \## Docker

# 

# The application was containerized using Docker.

# 

# Docker packages the application, dependencies, model and runtime environment into a reproducible container.

# 

# Run locally with:

# 

# ```bash

# docker compose up -d --build

# ```

# 

# \## Deployment

# 

# The application was deployed to the cloud using Render.

# 

# The cloud service builds and runs the Docker container and exposes the FastAPI application through a public endpoint.

# 

# \## Monitoring

# 

# Prediction logging was implemented to monitor model usage in production.

# 

# The API records information such as:

# 

# \- Prediction timestamp

# \- Churn classification

# \- Churn probability

# \- Customer tenure

# \- Monthly charges

# 

# These logs provide the foundation for monitoring prediction behavior and detecting potential data drift or model drift.

# 

# \## MLOps Workflow

# 

# ```text

# Development

# &#x20;    ↓

# Git

# &#x20;    ↓

# GitHub

# &#x20;    ↓

# Docker

# &#x20;    ↓

# Cloud Deployment

# &#x20;    ↓

# FastAPI

# &#x20;    ↓

# Predictions

# &#x20;    ↓

# Logs / Monitoring

# ```

# 

# \## Future Improvements

# 

# \- Advanced data drift monitoring

# \- Model performance monitoring

# \- CI/CD pipeline

# \- Microsoft Azure deployment

