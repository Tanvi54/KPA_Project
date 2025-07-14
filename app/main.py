from fastapi import FastAPI
from .routes import bogie_checksheet, wheel_specifications
from . import models
from .database import engine

# Create tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# Include API routes
app.include_router(bogie_checksheet.router)
app.include_router(wheel_specifications.router)
