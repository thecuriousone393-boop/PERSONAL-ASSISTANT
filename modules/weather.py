# modules/weather.py
import requests
from config import OPENWEATHER_API_KEY

def get_weather_by_city(city):
    if not OPENWEATHER_API_KEY or OPENWEATHER_API_KEY == "YOUR_OPENWEATHER_API_KEY":
        return {"error": "No API key. Set OPENWEATHER_API_KEY in config.py"}
    if not city:
        return {"error": "City name required"}
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": OPENWEATHER_API_KEY, "units": "metric"}
    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code != 200:
            return {"error": f"API error {r.status_code}", "detail": r.json()}
        data = r.json()
        return {
            "city": data.get("name"),
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"]
        }
    except requests.RequestException as e:
        return {"error": "Network error", "detail": str(e)}
