"""
Prediction API routes
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, Dict, Any
from starlette.requests import Request


router = APIRouter()


class WeatherData(BaseModel):
    temperature: float
    precipitation: float
    humidity: float
    wind_speed: Optional[float] = 5.0


class SoilData(BaseModel):
    ph: float
    nitrogen: float
    potassium: float
    phosphorus: float


class SatelliteData(BaseModel):
    ndvi: float
    evi: float
    crop_type: str


class PredictionRequest(BaseModel):
    weather: WeatherData
    soil: SoilData
    satellite: SatelliteData


class PredictionResponse(BaseModel):
    predicted_yield: float
    unit: str
    confidence_lower: float
    confidence_upper: float
    features: Dict[str, Any]


def get_predictor(request: Request):
    """Dependency to get the predictor from app state"""
    if not hasattr(request.app.state, 'predictor') or request.app.state.predictor is None:
        raise HTTPException(status_code=500, detail="Model not initialized")
    return request.app.state.predictor


@router.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest, predictor=Depends(get_predictor)):
    """
    Predict crop yield from multimodal data
    
    - **weather**: Temperature (°C), Precipitation (mm), Humidity (%), Wind Speed (m/s)
    - **soil**: pH, Nitrogen (mg/kg), Potassium (mg/kg), Phosphorus (mg/kg)
    - **satellite**: NDVI (0-1), EVI (0-1), Crop Type (maize/wheat/rice/beans/soybean)
    """
    try:
        prediction = predictor.predict(
            weather_data=request.weather.dict(),
            soil_data=request.soil.dict(),
            satellite_data=request.satellite.dict()
        )
        return PredictionResponse(**prediction)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@router.post("/predict/batch")
async def predict_batch(requests: list[PredictionRequest], predictor=Depends(get_predictor)):
    """Batch prediction for multiple inputs"""
    try:
        predictions = []
        for req in requests:
            pred = predictor.predict(
                weather_data=req.weather.dict(),
                soil_data=req.soil.dict(),
                satellite_data=req.satellite.dict()
            )
            predictions.append(pred)
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/explain/{prediction_id}")
async def explain_prediction(weather_data: Dict[str, float],
                            soil_data: Dict[str, float],
                            satellite_data: Dict[str, float],
                            predictor=Depends(get_predictor)):
    """
    Get explainable insights for a prediction
    Shows feature importance and contributions
    """
    try:
        explanation = predictor.explain_prediction(
            weather_data=weather_data,
            soil_data=soil_data,
            satellite_data=satellite_data
        )
        return explanation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/models/info")
async def get_model_info(predictor=Depends(get_predictor)):
    """Get information about the model"""
    return {
        "model_name": "Multimodal Crop Yield Predictor",
        "version": "1.0.0",
        "features": predictor.feature_names,
        "supported_crops": ["maize", "wheat", "rice", "beans", "soybean"],
        "is_trained": predictor.is_trained,
        "feature_importance": predictor.get_feature_importance()
    }
