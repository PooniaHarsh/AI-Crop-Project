"""
Crop Yield Predictor Model
Combines weather, soil, and satellite data for prediction
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import os
from typing import Dict, Tuple, List, Any


class CropYieldPredictor:
    """
    Multimodal crop yield prediction model using multiple data sources
    - Weather data (temperature, precipitation, humidity)
    - Soil data (pH, nitrogen, potassium, phosphorus)
    - Satellite data (NDVI, EVI, crop type)
    """
    
    def __init__(self):
        self.rf_model = None
        self.scaler = StandardScaler()
        self.feature_names = [
            'temperature', 'precipitation', 'humidity', 'wind_speed',
            'soil_ph', 'nitrogen', 'potassium', 'phosphorus',
            'ndvi', 'evi', 'crop_type_encoded'
        ]
        self.is_trained = False
        self._initialize_dummy_model()
    
    def _initialize_dummy_model(self):
        """Initialize a dummy model for demonstration"""
        # Create a simple Random Forest model
        self.rf_model = RandomForestRegressor(
            n_estimators=100,
            max_depth=15,
            random_state=42
        )
        
        # Generate synthetic training data for demo
        X_train = np.random.randn(100, len(self.feature_names)) * 10 + 50
        X_train = np.clip(X_train, 0, 100)
        y_train = (
            X_train[:, 0] * 1.5 +  # temperature
            X_train[:, 1] * 0.8 +  # precipitation
            X_train[:, 3] * 0.5 -  # wind_speed
            X_train[:, 4] * 0.3 +  # soil_ph
            X_train[:, 5] * 2.0 +  # nitrogen
            X_train[:, 8] * 30 +   # ndvi
            np.random.randn(100) * 5
        )
        y_train = np.clip(y_train, 1000, 8000)
        
        self.rf_model.fit(X_train, y_train)
        self.scaler.fit(X_train)
        self.is_trained = True
    
    def predict(self, weather_data: Dict[str, float], 
                soil_data: Dict[str, float],
                satellite_data: Dict[str, float]) -> Dict[str, Any]:
        """
        Make crop yield prediction from multimodal data
        
        Args:
            weather_data: Dict with temperature, precipitation, humidity, wind_speed
            soil_data: Dict with ph, nitrogen, potassium, phosphorus
            satellite_data: Dict with ndvi, evi, crop_type
        
        Returns:
            Dictionary with prediction and confidence intervals
        """
        try:
            # Prepare input features
            features = self._prepare_features(weather_data, soil_data, satellite_data)
            
            # Scale features
            features_scaled = self.scaler.transform([features])
            
            # Make prediction
            yield_prediction = self.rf_model.predict(features_scaled)[0]
            
            # Calculate confidence interval (simplified)
            predictions_variance = self.rf_model.predict(features_scaled)[0] * 0.1
            
            return {
                'predicted_yield': float(max(yield_prediction, 0)),
                'unit': 'kg/hectare',
                'confidence_lower': float(max(yield_prediction - predictions_variance, 0)),
                'confidence_upper': float(yield_prediction + predictions_variance),
                'features': {
                    'weather': weather_data,
                    'soil': soil_data,
                    'satellite': satellite_data
                }
            }
        except Exception as e:
            raise ValueError(f"Prediction failed: {str(e)}")
    
    def _prepare_features(self, weather_data: Dict[str, float],
                         soil_data: Dict[str, float],
                         satellite_data: Dict[str, float]) -> np.ndarray:
        """Combine multimodal data into feature vector"""
        features = [
            weather_data.get('temperature', 20),
            weather_data.get('precipitation', 50),
            weather_data.get('humidity', 60),
            weather_data.get('wind_speed', 5),
            soil_data.get('ph', 7),
            soil_data.get('nitrogen', 50),
            soil_data.get('potassium', 100),
            soil_data.get('phosphorus', 30),
            satellite_data.get('ndvi', 0.6),
            satellite_data.get('evi', 0.4),
            self._encode_crop_type(satellite_data.get('crop_type', 'maize'))
        ]
        return np.array(features)
    
    def _encode_crop_type(self, crop_type: str) -> float:
        """Encode categorical crop type to numerical value"""
        crop_encoding = {
            'maize': 1.0,
            'wheat': 2.0,
            'rice': 3.0,
            'beans': 4.0,
            'soybean': 5.0
        }
        return crop_encoding.get(crop_type.lower(), 1.0)
    
    def get_feature_importance(self) -> Dict[str, float]:
        """Get feature importance from the model"""
        if not self.is_trained:
            return {}
        
        importances = self.rf_model.feature_importances_
        return {name: float(imp) for name, imp in zip(self.feature_names, importances)}
    
    def explain_prediction(self, weather_data: Dict[str, float],
                          soil_data: Dict[str, float],
                          satellite_data: Dict[str, float]) -> Dict[str, Any]:
        """
        Explain the prediction with feature contributions
        """
        features = self._prepare_features(weather_data, soil_data, satellite_data)
        importances = self.get_feature_importance()
        
        # Calculate feature contributions (simplified)
        contributions = {
            name: float(features[i] * importances.get(name, 0))
            for i, name in enumerate(self.feature_names)
        }
        
        return {
            'feature_importance': importances,
            'feature_contributions': contributions,
            'top_factors': sorted(contributions.items(), key=lambda x: abs(x[1]), reverse=True)[:5]
        }
