from fastapi import FastAPI

app = FastAPI(
    title="Multilingual Text Preprocessing Engine",
    description="A modular FastAPI system for Arabic and English text preprocessing.",
    version="1.0.0"
)

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