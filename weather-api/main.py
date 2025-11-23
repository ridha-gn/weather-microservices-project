from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI(title="Weather API")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fake weather data
weather_data = {
    "london": {"city": "London", "temperature": 15, "condition": "Cloudy", "humidity": 78},
    "paris": {"city": "Paris", "temperature": 18, "condition": "Sunny", "humidity": 65},
    "newyork": {"city": "New York", "temperature": 12, "condition": "Rainy", "humidity": 85},
    "tokyo": {"city": "Tokyo", "temperature": 22, "condition": "Clear", "humidity": 60},
}

@app.get("/")
async def root():
    return {"message": "Weather API is running"}

@app.get("/weather")
async def get_weather():
    """Get weather for all cities"""
    return weather_data

@app.get("/weather/{city}")
async def get_city_weather(city: str):
    """Get weather for specific city"""
    city = city.lower()
    if city in weather_data:
        return weather_data[city]
    else:
        # Return random weather for unknown cities
        conditions = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy"]
        return {
            "city": city.title(),
            "temperature": random.randint(-5, 35),
            "condition": random.choice(conditions),
            "humidity": random.randint(30, 90)
        }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
