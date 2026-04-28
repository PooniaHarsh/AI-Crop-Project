import { useState } from 'react'
import './PredictionForm.css'

export default function PredictionForm({ onSubmit, loading }) {
  const [formData, setFormData] = useState({
    weather: {
      temperature: 22,
      precipitation: 60,
      humidity: 65,
      wind_speed: 5,
    },
    soil: {
      ph: 7.0,
      nitrogen: 80,
      potassium: 120,
      phosphorus: 40,
    },
    satellite: {
      ndvi: 0.65,
      evi: 0.45,
      crop_type: 'maize',
    },
  })

  const handleWeatherChange = (e) => {
    const { name, value } = e.target
    setFormData({
      ...formData,
      weather: {
        ...formData.weather,
        [name]: parseFloat(value) || 0,
      },
    })
  }

  const handleSoilChange = (e) => {
    const { name, value } = e.target
    setFormData({
      ...formData,
      soil: {
        ...formData.soil,
        [name]: parseFloat(value) || 0,
      },
    })
  }

  const handleSatelliteChange = (e) => {
    const { name, value } = e.target
    if (name === 'crop_type') {
      setFormData({
        ...formData,
        satellite: {
          ...formData.satellite,
          [name]: value,
        },
      })
    } else {
      setFormData({
        ...formData,
        satellite: {
          ...formData.satellite,
          [name]: parseFloat(value) || 0,
        },
      })
    }
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    onSubmit(formData)
  }

  return (
    <form className="prediction-form" onSubmit={handleSubmit}>
      <h2>Farm Data Input</h2>

      {/* Weather Data Section */}
      <fieldset className="form-section">
        <legend>🌤️ Weather Data</legend>
        <div className="form-grid">
          <div className="form-group">
            <label htmlFor="temperature">Temperature (°C)</label>
            <input
              type="number"
              id="temperature"
              name="temperature"
              value={formData.weather.temperature}
              onChange={handleWeatherChange}
              step="0.1"
              min="-10"
              max="50"
              disabled={loading}
            />
            <span className="example">Range: -10 to 50°C</span>
          </div>

          <div className="form-group">
            <label htmlFor="precipitation">Precipitation (mm)</label>
            <input
              type="number"
              id="precipitation"
              name="precipitation"
              value={formData.weather.precipitation}
              onChange={handleWeatherChange}
              step="0.1"
              min="0"
              max="500"
              disabled={loading}
            />
            <span className="example">Range: 0 to 500mm</span>
          </div>

          <div className="form-group">
            <label htmlFor="humidity">Humidity (%)</label>
            <input
              type="number"
              id="humidity"
              name="humidity"
              value={formData.weather.humidity}
              onChange={handleWeatherChange}
              step="0.1"
              min="0"
              max="100"
              disabled={loading}
            />
            <span className="example">Range: 0 to 100%</span>
          </div>

          <div className="form-group">
            <label htmlFor="wind_speed">Wind Speed (m/s)</label>
            <input
              type="number"
              id="wind_speed"
              name="wind_speed"
              value={formData.weather.wind_speed}
              onChange={handleWeatherChange}
              step="0.1"
              min="0"
              max="20"
              disabled={loading}
            />
            <span className="example">Range: 0 to 20 m/s</span>
          </div>
        </div>
      </fieldset>

      {/* Soil Data Section */}
      <fieldset className="form-section">
        <legend>🌱 Soil Data</legend>
        <div className="form-grid">
          <div className="form-group">
            <label htmlFor="ph">pH Level</label>
            <input
              type="number"
              id="ph"
              name="ph"
              value={formData.soil.ph}
              onChange={handleSoilChange}
              step="0.1"
              min="4"
              max="10"
              disabled={loading}
            />
            <span className="example">Range: 4 to 10</span>
          </div>

          <div className="form-group">
            <label htmlFor="nitrogen">Nitrogen (mg/kg)</label>
            <input
              type="number"
              id="nitrogen"
              name="nitrogen"
              value={formData.soil.nitrogen}
              onChange={handleSoilChange}
              step="1"
              min="0"
              max="300"
              disabled={loading}
            />
            <span className="example">Range: 0 to 300</span>
          </div>

          <div className="form-group">
            <label htmlFor="potassium">Potassium (mg/kg)</label>
            <input
              type="number"
              id="potassium"
              name="potassium"
              value={formData.soil.potassium}
              onChange={handleSoilChange}
              step="1"
              min="0"
              max="300"
              disabled={loading}
            />
            <span className="example">Range: 0 to 300</span>
          </div>

          <div className="form-group">
            <label htmlFor="phosphorus">Phosphorus (mg/kg)</label>
            <input
              type="number"
              id="phosphorus"
              name="phosphorus"
              value={formData.soil.phosphorus}
              onChange={handleSoilChange}
              step="1"
              min="0"
              max="100"
              disabled={loading}
            />
            <span className="example">Range: 0 to 100</span>
          </div>
        </div>
      </fieldset>

      {/* Satellite Data Section */}
      <fieldset className="form-section">
        <legend>📡 Satellite Data</legend>
        <div className="form-grid">
          <div className="form-group">
            <label htmlFor="ndvi">NDVI Index</label>
            <input
              type="number"
              id="ndvi"
              name="ndvi"
              value={formData.satellite.ndvi}
              onChange={handleSatelliteChange}
              step="0.01"
              min="-1"
              max="1"
              disabled={loading}
            />
            <span className="example">Range: -1 to 1</span>
          </div>

          <div className="form-group">
            <label htmlFor="evi">EVI Index</label>
            <input
              type="number"
              id="evi"
              name="evi"
              value={formData.satellite.evi}
              onChange={handleSatelliteChange}
              step="0.01"
              min="-1"
              max="1"
              disabled={loading}
            />
            <span className="example">Range: -1 to 1</span>
          </div>

          <div className="form-group full-width">
            <label htmlFor="crop_type">Crop Type</label>
            <select
              id="crop_type"
              name="crop_type"
              value={formData.satellite.crop_type}
              onChange={handleSatelliteChange}
              disabled={loading}
            >
              <option value="maize">Maize</option>
              <option value="wheat">Wheat</option>
              <option value="rice">Rice</option>
              <option value="beans">Beans</option>
              <option value="soybean">Soybean</option>
            </select>
          </div>
        </div>
      </fieldset>

      <button type="submit" className="submit-button" disabled={loading}>
        {loading ? 'Predicting...' : '🚀 Predict Crop Yield'}
      </button>
    </form>
  )
}
