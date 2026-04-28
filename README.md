# AI-Driven Crop Yield Prediction System

An intelligent, multimodal crop yield prediction system that leverages weather data, soil properties, and satellite imagery to provide accurate yield forecasts with explainable insights.

![Crop Yield Prediction UI](./frontend/public/assets/kreamer_feed_inc_cover.jpeg)

## 🌾 Project Overview

This full-stack application combines:
- **Weather Data**: Temperature, precipitation, humidity, wind speed
- **Soil Properties**: pH, nitrogen, potassium, phosphorus content
- **Satellite Imagery**: NDVI and EVI vegetation indices

Machine learning models analyze these multimodal inputs to predict crop yields and provide explainable recommendations for farmers.

## 🚀 Getting Started

### Prerequisites
- **Python 3.8+** 
- **Node.js 16+** and npm
- Virtual environment (venv or conda)

### Installation & Setup

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd "AI project"
```

#### 2. Backend Setup

**Step 1: Activate Virtual Environment**
```bash
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate  # On Windows
```

**Step 2: Install Dependencies**
```bash
cd backend
pip install -r requirements.txt
```

**Step 3: Start Backend Server**
```bash
python -m uvicorn main:app --reload --port 5000
```
Backend will run on: `http://127.0.0.1:5000`

#### 3. Frontend Setup

**Step 1: Install Dependencies**
```bash
cd frontend
npm install
```

**Step 2: Start Frontend Development Server**
```bash
npm run dev
```
Frontend will run on: `http://localhost:3000`

### Running Both Servers Simultaneously

You can start both servers in separate terminal windows:

**Terminal 1 (Backend):**
```bash
cd backend
python -m uvicorn main:app --reload --port 5000
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

Then navigate to `http://localhost:3000` in your browser to access the application.

### API Endpoints

- **Health Check**: `http://127.0.0.1:5000/`
- **Predictions**: `http://127.0.0.1:5000/api/predict` (POST)
- **Models**: `http://127.0.0.1:5000/api/models` (GET)

### Building for Production

**Frontend:**
```bash
cd frontend
npm run build
```

## 📁 Project Structure

- `Multimodal ML Specialists
- Agricultural Data Scientists

## 🙏 Acknowledgments

- Agricultural data sources
- Satellite imagery providers
- Open-source ML community
- FastAPI and React communities

---

**Last Updated**: April 2026 
**Version**: 1.0.0
# AI-Crop-Project
