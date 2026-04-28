"""
AI-Driven Multimodal Crop Yield Prediction API
Uses integrated weather, soil, and satellite data with explainable learning
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import numpy as np
from models.yield_predictor import CropYieldPredictor
from routes.predictions import router as predictions_router

app = FastAPI(
    title="Crop Yield Prediction API",
    description="AI-driven multimodal crop yield prediction using weather, soil, and satellite data",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the ML model
try:
    predictor = CropYieldPredictor()
    app.state.predictor = predictor
except Exception as e:
    print(f"Warning: Could not initialize ML model: {e}")
    app.state.predictor = None


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Crop Yield Prediction API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "predict": "/api/predict",
            "models": "/api/models"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


# Include prediction routes
app.include_router(predictions_router, prefix="/api", tags=["predictions"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
