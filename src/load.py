"""Chargement des données dans SQLite."""

import sqlite3
from pathlib import Path
from typing import List


def initialiser_base(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS destinations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ville TEXT UNIQUE NOT NULL,
            pays TEXT,
            latitude REAL,
            longitude REAL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            destination_id INTEGER,
            temperature REAL,
            humidite INTEGER,
            precipitation REAL,
            vent REAL,
            code_meteo INTEGER,
            date_observation TEXT,
            FOREIGN KEY (destination_id) REFERENCES destinations(id)
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_obs_date ON observations(date_observation)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_obs_dest ON observations(destination_id)")
    conn.commit()
    return conn


def charger_destinations(conn: sqlite3.Connection, destinations: list) -> None:
    for d in destinations:
        conn.execute(
            "INSERT OR IGNORE INTO destinations (ville, pays, latitude, longitude) VALUES (?, ?, ?, ?)",
            (d["ville"], d["pays"], d["latitude"], d["longitude"]),
        )
    conn.commit()


def charger_observations(conn: sqlite3.Connection, observations: List[dict]) -> int:
    count = 0
    for obs in observations:
        if not obs:
            continue
        cur = conn.execute("SELECT id FROM destinations WHERE ville = ?", (obs["ville"],))
        row = cur.fetchone()
        if not row:
            continue
        dest_id = row[0]
        conn.execute(
            """INSERT INTO observations 
               (destination_id, temperature, humidite, precipitation, vent, code_meteo, date_observation)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                dest_id,
                obs["temperature"],
                obs["humidite"],
                obs["precipitation"],
                obs["vent"],
                obs["code_meteo"],
                obs["date_observation"],
            ),
        )
        count += 1
    conn.commit()
    return count
