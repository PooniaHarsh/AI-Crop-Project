import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ComposedChart } from 'recharts'
import './ResultVisualization.css'

export default function ResultVisualization({ prediction }) {
  if (!prediction || !prediction.features) return null

  const { predicted_yield, confidence_lower, confidence_upper, unit } = prediction

  // Data for yield visualization
  const yieldData = [
    {
      name: 'Predictions',
      'Lower Bound': Math.round(confidence_lower),
      'Predicted': Math.round(predicted_yield),
      'Upper Bound': Math.round(confidence_upper),
    },
  ]

  // Data for feature contributions (sample)
  const featureData = [
    { name: 'Temperature', value: 15 },
    { name: 'Precipitation', value: 12 },
    { name: 'Nitrogen', value: 18 },
    { name: 'NDVI', value: 20 },
    { name: 'pH Level', value: 8 },
  ]

  // Data for confidence interval
  const confidenceData = [
    {
      label: 'Lower',
      value: Math.round(confidence_lower),
      fill: '#fbbf24',
    },
    {
      label: 'Predicted',
      value: Math.round(predicted_yield),
      fill: '#10b981',
    },
    {
      label: 'Upper',
      value: Math.round(confidence_upper),
      fill: '#3b82f6',
    },
  ]

  return (
    <div className="result-visualization">
      <h2>📊 Prediction Results</h2>

      {/* Main Yield Prediction */}
      <div className="prediction-summary">
        <div className="yield-card main">
          <h3>Predicted Crop Yield</h3>
          <div className="yield-value">
            {Math.round(predicted_yield).toLocaleString()}
          </div>
          <div className="yield-unit">{unit}</div>
        </div>

        <div className="confidence-cards">
          <div className="yield-card">
            <h4>Lower Bound (95% CI)</h4>
            <div className="yield-value secondary">
              {Math.round(confidence_lower).toLocaleString()}
            </div>
          </div>
          <div className="yield-card">
            <h4>Upper Bound (95% CI)</h4>
            <div className="yield-value secondary">
              {Math.round(confidence_upper).toLocaleString()}
            </div>
          </div>
        </div>
      </div>

      {/* Yield Range Visualization */}
      <div className="chart-container">
        <h3>Confidence Interval</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={confidenceData} layout="vertical">
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis type="number" />
            <YAxis dataKey="label" type="category" width={80} />
            <Tooltip />
            <Bar dataKey="value" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Feature Importance */}
      <div className="chart-container">
        <h3>Feature Importance</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={featureData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" angle={-45} textAnchor="end" height={100} />
            <YAxis />
            <Tooltip />
            <Bar dataKey="value" fill="#10b981" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Input Data Summary */}
      <div className="input-summary">
        <h3>Input Parameters Summary</h3>
        <div className="summary-grid">
          <div className="summary-item">
            <span className="label">🌤️ Temperature</span>
            <span className="value">{prediction.features.weather.temperature}°C</span>
          </div>
          <div className="summary-item">
            <span className="label">💧 Precipitation</span>
            <span className="value">{prediction.features.weather.precipitation}mm</span>
          </div>
          <div className="summary-item">
            <span className="label">☁️ Humidity</span>
            <span className="value">{prediction.features.weather.humidity}%</span>
          </div>
          <div className="summary-item">
            <span className="label">💨 Wind Speed</span>
            <span className="value">{prediction.features.weather.wind_speed}m/s</span>
          </div>
          <div className="summary-item">
            <span className="label">🌱 Soil pH</span>
            <span className="value">{prediction.features.soil.ph}</span>
          </div>
          <div className="summary-item">
            <span className="label">🧪 Nitrogen</span>
            <span className="value">{prediction.features.soil.nitrogen}mg/kg</span>
          </div>
          <div className="summary-item">
            <span className="label">📡 NDVI</span>
            <span className="value">{prediction.features.satellite.ndvi.toFixed(2)}</span>
          </div>
          <div className="summary-item">
            <span className="label">🌾 Crop Type</span>
            <span className="value">{prediction.features.satellite.crop_type}</span>
          </div>
        </div>
      </div>
    </div>
  )
}
