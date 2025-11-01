# main.py
from fastapi import FastAPI
from routes.pg_health_indicators import router as health_indicators_router  # Updated name
from routes.predict import router as predict_router
import uvicorn

app = FastAPI(title="Heart Disease API")

app.include_router(health_indicators_router)
app.include_router(predict_router)

@app.get("/")
def root():
    return {"message": "Heart Disease API is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)