from fastapi import FastAPI
from app.api.categorize import router as categorize_router

app = FastAPI(title="Smart Categorizer")

app.include_router(categorize_router)
