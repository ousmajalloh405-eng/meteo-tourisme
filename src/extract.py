"""Extraction des données météo via l'API Open-Meteo (gratuite, sans clé)."""

import requests
from datetime import datetime
from typing import Optional


def extraire_meteo(latitude: float, longitude: float, ville: str) -> Optional[dict]:
    """Récupère la météo actuelle pour une destination."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m,weather_code",
        "timezone": "auto",
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        current = data.get("current", {})
        return {
            "ville": ville,
            "temperature": current.get("temperature_2m"),
            "humidite": current.get("relative_humidity_2m"),
            "precipitation": current.get("precipitation", 0),
            "vent": current.get("wind_speed_10m"),
            "code_meteo": current.get("weather_code"),
            "date_observation": datetime.now().isoformat(),
        }
    except Exception as e:
        print(f"Erreur extraction {ville}: {e}")
        return None
