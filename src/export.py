"""Export des données météo en JSON lisible."""

import json
import sqlite3
from pathlib import Path


def exporter_json(db_path: Path, json_path: Path) -> None:
    """Exporte destinations + observations en fichier JSON."""
    if not db_path.exists():
        print("Base de données introuvable.")
        return

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    destinations = [dict(row) for row in conn.execute("SELECT * FROM destinations")]
    observations = [dict(row) for row in conn.execute("""
        SELECT d.ville, d.pays, o.temperature, o.humidite,
               o.precipitation, o.vent, o.code_meteo, o.date_observation
        FROM observations o
        JOIN destinations d ON o.destination_id = d.id
        ORDER BY o.date_observation DESC
    """)]

    data = {
        "destinations": destinations,
        "observations": observations,
        "total_observations": len(observations),
    }

    json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Export JSON créé : {json_path} ({len(observations)} observations)")
    conn.close()
