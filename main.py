# main.py
from fastapi import FastAPI
from routes.health_indicators import router as health_indicators_router  # Fixed: no formative_1_ml_pipeline
from routes.predict import router as predict_router  # Our new route
import uvicorn

app = FastAPI(title="Heart Disease API")

app.include_router(health_indicators_router)
app.include_router(predict_router)  # Add prediction

@app.get("/")
def root():
    return {"message": "Heart Disease API is running"}
app.include_router(health_indicators_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)