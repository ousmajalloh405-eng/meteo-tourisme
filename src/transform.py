"""Transformation et nettoyage des données météo."""

from typing import Optional


def transformer(donnee: dict) -> Optional[dict]:
    """Nettoie et normalise une observation météo."""
    if not donnee:
        return None

    temperature = donnee.get("temperature")
    if temperature is None:
        return None

    return {
        "ville": donnee["ville"].strip().title(),
        "temperature": round(float(temperature), 1),
        "humidite": int(donnee.get("humidite") or 0),
        "precipitation": round(float(donnee.get("precipitation") or 0), 1),
        "vent": round(float(donnee.get("vent") or 0), 1),
        "code_meteo": int(donnee.get("code_meteo") or 0),
        "date_observation": donnee["date_observation"],
    }
