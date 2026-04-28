# AI-Driven Crop Yield Prediction System

An intelligent, multimodal crop yield prediction system that leverages weather data, soil properties, and satellite imagery to provide accurate yield forecasts with explainable insights.

## 🌾 Project Overview

This full-stack application combines:
- **Weather Data**: Temperature, precipitation, humidity, wind speed
- **Soil Properties**: pH, nitrogen, potassium, phosphorus content
- **Satellite Imagery**: NDVI and EVI vegetation indices

Machine learning models analyze these multimodal inputs to predict crop yields and provide explainable recommendations for farmers.

## 🏗️ Architecture

```
AI project/
├── backend/                    # Python FastAPI backend
│   ├── main.py                # FastAPI application
│   ├── models/                # ML models
│   │   └── yield_predictor.py # Crop yield prediction model
│   ├── routes/                # API routes
│   │   └── predictions.py     # Prediction endpoints
│   ├── utils/                 # Utility functions
│   │   └── data_processor.py  # Data processing utilities
│   ├── data/                  # Data directory
│   └── requirements.txt       # Python dependencies
│
├── frontend/                  # React Vite application
│   ├── src/
│   │   ├── App.jsx           # Main application component
│   │   ├── main.jsx          # React entry point
│   │   ├── components/       # Reusable components
│   │   │   ├── PredictionForm.jsx      # Input form
│   │   │   └── ResultVisualization.jsx # Results display
│   │   └── styles/           # CSS files
│   ├── public/               # Static assets
│   ├── package.json          # npm dependencies
│   └── vite.config.js        # Vite configuration
│
└── .github/
    └── copilot-instructions.md # Project instructions
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. **Create Python virtual environment**:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API server**:
   ```bash
   python main.py
   # API runs on http://localhost:5000
   ```

### Frontend Setup

1. **Install dependencies**:
   ```bash
   cd frontend
   npm install
   ```

2. **Start development server**:
   ```bash
   npm run dev
   # Frontend runs on http://localhost:3000
   ```

3. **Build for production**:
   ```bash
   npm run build
   ```

## 📊 API Endpoints

### Health Check
- `GET /` - API info
- `GET /health` - Health status

### Predictions
- `POST /api/predict` - Single prediction
- `POST /api/predict/batch` - Batch predictions
- `GET /api/models/info` - Model information
- `GET /api/explain` - Explainable insights

## 🎯 Usage Example

### Making a Prediction

```bash
curl -X POST "http://localhost:5000/api/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "weather": {
      "temperature": 22,
      "precipitation": 60,
      "humidity": 65,
      "wind_speed": 5
    },
    "soil": {
      "ph": 7.0,
      "nitrogen": 80,
      "potassium": 120,
      "phosphorus": 40
    },
    "satellite": {
      "ndvi": 0.65,
      "evi": 0.45,
      "crop_type": "maize"
    }
  }'
```

## 🔍 Response Format

```json
{
  "predicted_yield": 5234.5,
  "unit": "kg/hectare",
  "confidence_lower": 4711.05,
  "confidence_upper": 5757.95,
  "features": {
    "weather": {...},
    "soil": {...},
    "satellite": {...}
  }
}
```

## 🤖 Supported Crops

- Maize
- Wheat
- Rice
- Beans
- Soybean

## 📈 Features

- **Real-time Predictions**: Get yield forecasts instantly
- **Multimodal Analysis**: Combines weather, soil, and satellite data
- **Explainable AI**: Understand which factors influence predictions
- **Batch Processing**: Process multiple predictions efficiently
- **Interactive Dashboard**: User-friendly web interface
- **Data Visualization**: Charts and graphs for insights
- **RESTful API**: Easy integration with external systems

## 🛠️ Technology Stack

### Backend
- **FastAPI**: Modern web framework
- **TensorFlow/Scikit-learn**: Machine learning
- **Pandas/NumPy**: Data processing
- **Pydantic**: Data validation

### Frontend
- **React 18**: UI library
- **Vite**: Build tool
- **Recharts**: Data visualization
- **Tailwind CSS**: Styling

## 📝 Project Structure Details

### Backend Modules

**`models/yield_predictor.py`**
- Core ML model for yield prediction
- Feature engineering
- Model training and inference
- Feature importance calculation

**`routes/predictions.py`**
- API endpoints for predictions
- Request/response validation
- Error handling

**`utils/data_processor.py`**
- Data normalization
- Missing value handling
- Outlier detection
- Data merging utilities

### Frontend Components

**`PredictionForm.jsx`**
- Input form for farm data
- Real-time validation
- Responsive design

**`ResultVisualization.jsx`**
- Yield prediction display
- Confidence interval charts
- Feature importance visualization
- Input summary

## 🔧 Configuration

### Backend Environment Variables
Create `.env` file in backend directory:
```
DATABASE_URL=postgresql://user:password@localhost/cropdb
ML_MODEL_PATH=./models/predictor_model.pkl
DEBUG=False
```

### Frontend Environment Variables
Create `.env` in frontend directory:
```
VITE_API_URL=http://localhost:5000
VITE_ENV=development
```

## 📦 Dependencies

### Backend (Python)
- fastapi==0.104.1
- uvicorn==0.24.0
- scikit-learn==1.3.2
- tensorflow==2.14.0
- pandas==2.1.3
- numpy==1.24.3

### Frontend (Node.js)
- react@^18.2.0
- recharts@^2.10.0
- axios@^1.6.0
- vite@^5.0.0

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 📚 Documentation

For detailed API documentation, visit:
- Swagger UI: `http://localhost:5000/docs`
- ReDoc: `http://localhost:5000/redoc`

## 🚢 Deployment

### Docker

1. **Build Docker image**:
   ```bash
   docker build -t crop-yield-predictor .
   ```

2. **Run container**:
   ```bash
   docker run -p 5000:5000 crop-yield-predictor
   ```

### Cloud Deployment

- **Backend**: Deploy FastAPI app to Heroku, AWS Lambda, or Google Cloud Run
- **Frontend**: Deploy React build to Vercel, Netlify, or AWS S3 + CloudFront

## 📊 Data Format

### Weather Data
| Field | Range | Unit |
|-------|-------|------|
| Temperature | -10 to 50 | °C |
| Precipitation | 0 to 500 | mm |
| Humidity | 0 to 100 | % |
| Wind Speed | 0 to 20 | m/s |

### Soil Data
| Field | Range | Unit |
|-------|-------|------|
| pH | 4 to 10 | - |
| Nitrogen | 0 to 300 | mg/kg |
| Potassium | 0 to 300 | mg/kg |
| Phosphorus | 0 to 100 | mg/kg |

### Satellite Data
| Field | Range | Unit |
|-------|-------|------|
| NDVI | -1 to 1 | - |
| EVI | -1 to 1 | - |

## 🎓 Model Explanation

The prediction model uses Random Forest regression with feature importance analysis. Key factors affecting yield:

1. **Temperature** (15%): Optimal range 18-28°C
2. **NDVI** (20%): Higher vegetation index = better yield
3. **Nitrogen** (18%): Essential nutrient for growth
4. **Precipitation** (12%): Adequate water crucial
5. **Soil pH** (8%): Neutral pH optimal

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- AI Development Team
- Multimodal ML Specialists
- Agricultural Data Scientists

## 🙏 Acknowledgments

- Agricultural data sources
- Satellite imagery providers
- Open-source ML community
- FastAPI and React communities

## 📞 Support

For questions or issues:
- Create an Issue on GitHub
- Contact: support@cropyieldprediction.com
- Documentation: https://docs.cropyieldprediction.com

---

**Last Updated**: April 2024  
**Version**: 1.0.0
# AI-Crop-Project
