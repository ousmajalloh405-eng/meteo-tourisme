"""Pipeline ETL météo pour le tourisme."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from config import DESTINATIONS
from extract import extraire_meteo
from transform import transformer
from load import initialiser_base, charger_destinations, charger_observations


DB_PATH = Path(__file__).parent / "data" / "meteo.db"


def run_pipeline():
    print("=== Pipeline météo tourisme ===\n")

    conn = initialiser_base(DB_PATH)
    charger_destinations(conn, DESTINATIONS)
    print(f"Destinations chargées : {len(DESTINATIONS)}")

    observations = []
    for dest in DESTINATIONS:
        print(f"Extraction : {dest['ville']}...")
        brut = extraire_meteo(dest["latitude"], dest["longitude"], dest["ville"])
        propre = transformer(brut)
        if propre:
            observations.append(propre)
            print(f"  → {propre['temperature']}°C, humidité {propre['humidite']}%")
        else:
            print("  → échec")

    nb = charger_observations(conn, observations)
    print(f"\n{nb} observations insérées dans {DB_PATH}")

    print("\n=== Dernières observations ===")
    cur = conn.execute("""
        SELECT d.ville, o.temperature, o.humidite, o.precipitation, o.date_observation
        FROM observations o
        JOIN destinations d ON o.destination_id = d.id
        ORDER BY o.date_observation DESC
        LIMIT 10
    """)
    for row in cur:
        print(f"{row[0]:15} | {row[1]}°C | hum. {row[2]}% | pluie {row[3]} mm")

    conn.close()
    print("\nPipeline terminé.")


if __name__ == "__main__":
    run_pipeline()
