"""
Data processing utilities for crop yield prediction
"""

import pandas as pd
import numpy as np
from typing import Tuple, List, Dict


class DataProcessor:
    """Process and prepare data for crop yield prediction"""
    
    @staticmethod
    def normalize_weather_data(weather_df: pd.DataFrame) -> pd.DataFrame:
        """
        Normalize weather data to standard ranges
        Temperature: -10 to 50°C
        Precipitation: 0 to 500mm
        Humidity: 0 to 100%
        Wind Speed: 0 to 20 m/s
        """
        weather_df['temperature'] = weather_df['temperature'].clip(-10, 50)
        weather_df['precipitation'] = weather_df['precipitation'].clip(0, 500)
        weather_df['humidity'] = weather_df['humidity'].clip(0, 100)
        weather_df['wind_speed'] = weather_df['wind_speed'].clip(0, 20)
        return weather_df
    
    @staticmethod
    def process_soil_data(soil_df: pd.DataFrame) -> pd.DataFrame:
        """Process and validate soil data"""
        soil_df['ph'] = soil_df['ph'].clip(4, 10)  # Valid pH range
        soil_df['nitrogen'] = soil_df['nitrogen'].clip(0, 300)
        soil_df['potassium'] = soil_df['potassium'].clip(0, 300)
        soil_df['phosphorus'] = soil_df['phosphorus'].clip(0, 100)
        return soil_df
    
    @staticmethod
    def process_satellite_data(sat_df: pd.DataFrame) -> pd.DataFrame:
        """Process satellite vegetation indices"""
        sat_df['ndvi'] = sat_df['ndvi'].clip(-1, 1)  # NDVI range
        sat_df['evi'] = sat_df['evi'].clip(-1, 1)    # EVI range
        return sat_df
    
    @staticmethod
    def merge_multimodal_data(weather_df: pd.DataFrame,
                              soil_df: pd.DataFrame,
                              satellite_df: pd.DataFrame,
                              yield_df: pd.DataFrame = None) -> pd.DataFrame:
        """
        Merge multimodal data into single DataFrame
        
        Args:
            weather_df: Weather data
            soil_df: Soil data
            satellite_df: Satellite data
            yield_df: Target yield data (optional)
        
        Returns:
            Merged DataFrame with all features
        """
        # Merge on common indices (assumes same indexing)
        merged = weather_df.copy()
        merged = merged.join(soil_df, how='inner')
        merged = merged.join(satellite_df, how='inner')
        
        if yield_df is not None:
            merged = merged.join(yield_df, how='inner')
        
        return merged
    
    @staticmethod
    def handle_missing_values(df: pd.DataFrame, strategy: str = 'mean') -> pd.DataFrame:
        """
        Handle missing values in data
        
        Args:
            df: Input DataFrame
            strategy: 'mean', 'median', 'forward_fill', 'backward_fill'
        """
        if strategy == 'mean':
            return df.fillna(df.mean())
        elif strategy == 'median':
            return df.fillna(df.median())
        elif strategy == 'forward_fill':
            return df.fillna(method='ffill')
        elif strategy == 'backward_fill':
            return df.fillna(method='bfill')
        return df
    
    @staticmethod
    def detect_outliers(df: pd.DataFrame, columns: List[str] = None, 
                       std_threshold: float = 3.0) -> pd.DataFrame:
        """
        Detect and flag outliers using standard deviation
        """
        if columns is None:
            columns = df.select_dtypes(include=[np.number]).columns
        
        outliers_mask = pd.DataFrame(False, index=df.index, columns=columns)
        
        for col in columns:
            mean = df[col].mean()
            std = df[col].std()
            outliers_mask[col] = np.abs(df[col] - mean) > std_threshold * std
        
        df['is_outlier'] = outliers_mask.any(axis=1)
        return df
