import { useState } from 'react'
import PredictionForm from './components/PredictionForm'
import ResultVisualization from './components/ResultVisualization'
import './App.css'

function App() {
  const [prediction, setPrediction] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handlePredict = async (formData) => {
    setLoading(true)
    setError(null)
    try {
      const response = await fetch('/api/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      })
      
      if (!response.ok) {
        throw new Error(`Prediction failed: ${response.statusText}`)
      }
      
      const data = await response.json()
      setPrediction(data)
    } catch (err) {
      setError(err.message)
      console.error('Prediction error:', err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>🌾 Crop Yield Prediction</h1>
        <p>AI-Driven Multimodal Prediction using Weather, Soil & Satellite Data</p>
      </header>

      <main className="app-main">
        <div className="content-wrapper">
          <section className="form-section">
            <PredictionForm onSubmit={handlePredict} loading={loading} />
          </section>

          {error && (
            <div className="error-message">
              <span>❌ Error: {error}</span>
            </div>
          )}

          {prediction && (
            <section className="results-section">
              <ResultVisualization prediction={prediction} />
            </section>
          )}

          {!prediction && !error && (
            <section className="empty-state">
              <div className="empty-state-content">
                <p>📊 Enter farm data to get yield predictions</p>
              </div>
            </section>
          )}
        </div>
      </main>

      <footer className="app-footer">
        <p>© 2026 Crop Yield Prediction System | Powered by AIML Group (Harsh, Anshul, Bhavik, Aditi)</p>
      </footer>
    </div>
  )
}

export default App
