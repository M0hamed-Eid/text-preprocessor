from fastapi import FastAPI
from src.routers.preprocess_router import router as preprocess_router

app = FastAPI(
    title="Multilingual Text Preprocessing Engine",
    description="A modular FastAPI system for Arabic and English text preprocessing.",
    version="1.0.0"
)

app.include_router(preprocess_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Multilingual Text Preprocessing Engine"
    }


@app.get("/health")
def health_check():
    return {
        "status": "running"
    }