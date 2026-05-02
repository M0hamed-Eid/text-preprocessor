from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.routers.preprocess_router import router as preprocess_router

app = FastAPI(
    title="Multilingual Text Preprocessing Engine",
    description="A modular FastAPI system for Arabic and English text preprocessing.",
    version="1.0.0"
)

# Static files
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Templates
templates = Jinja2Templates(directory="src/templates")

# API Router
app.include_router(preprocess_router)


@app.get("/")
def frontend_home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/health")
def health_check():
    return {"status": "running"}