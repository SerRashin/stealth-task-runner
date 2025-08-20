from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="Steal Task Runner", version="3.1.0")
app.include_router(router)
