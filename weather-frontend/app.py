from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Get API URL from environment or use default
API_URL = os.getenv('WEATHER_API_URL', 'http://weather-api:8000')

@app.route('/')
def index():
    try:
        # Fetch weather data from API
        response = requests.get(f"{API_URL}/weather")
        if response.status_code == 200:
            weather_data = response.json()
            return render_template('index.html', weather_data=weather_data, error=None)
        else:
            return render_template('index.html', weather_data=None, error="Failed to fetch weather data")
    except Exception as e:
        return render_template('index.html', weather_data=None, error=str(e))

@app.route('/health')
def health():
    return {"status": "healthy", "service": "weather-frontend"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
