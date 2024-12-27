from fastapi import FastAPI
from app.api.controller.lusha_controller import router as lusha_router

app = FastAPI()

# Register API routes
app.include_router(lusha_router, prefix="/api/v1")
