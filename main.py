# main.py
from fastapi import FastAPI
from routes.pg_router import router as pg_router
from routes.mongo_router import router as mongo_router
from routes.predict import router as predict_router  # ADD THIS
import uvicorn

app = FastAPI(title="Heart Disease API")

app.include_router(mongo_router)
app.include_router(pg_router)
app.include_router(predict_router)  # ADD THIS

@app.get("/")
def root():
    return {"message": "Heart Disease API is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)