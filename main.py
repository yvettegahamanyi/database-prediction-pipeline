# main.py
from fastapi import FastAPI
from formative_1_ml_pipeline.routes.health_indicators import router as health_indicators_router
from routes.predict import router as predict_router  # ADD THIS
import uvicorn

app = FastAPI(title="Heart Disease API")

app.include_router(health_indicators_router)
app.include_router(predict_router)  # ADD THIS

@app.get("/")
def root():
    return {"message": "Heart Disease API is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)