from fastapi import FastAPI
from .predict_router import router
from .load_model import load_artifacts

app = FastAPI(
    title="Bangalore Home Price Prediction API",
    version="1.0",
)

#load model and columns at startup
load_artifacts()

app.include_router(router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Welcome to the Bangalore Home Price Prediction API."}