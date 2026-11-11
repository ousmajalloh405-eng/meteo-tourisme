# Architecture — Pipeline Météo Tourisme

## Vue d'ensemble

Pipeline ETL qui collecte des données météo via une API publique, les nettoie et les stocke dans une base SQLite, avec export JSON lisible.

## Diagramme ETL

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  extract.py  │────▶│ transform.py │────▶│   load.py    │
│              │     │              │     │              │
│ Appel API    │     │ Nettoyage    │     │ Insertion    │
│ Open-Meteo   │     │ Normalisation│     │ SQLite       │
└─────────────┘     └─────────────┘     └──────┬───────┘
                                                  │
                                                  ▼
                                         ┌────────────────┐
                                         │  data/meteo.db │
                                         └────────┬───────┘
                                                  │
                                                  ▼
                                         ┌───────────────────┐
                                         │ meteo_export.json  │
                                         └───────────────────┘
```

## Composants

| Module | Responsabilité |
|--------|----------------|
| `src/config.py` | Liste des destinations (ville, coordonnées) |
| `src/extract.py` | Récupération des données via l’API Open-Meteo |
| `src/transform.py` | Nettoyage, arrondi, gestion des valeurs manquantes |
| `src/load.py` | Création des tables et insertion dans SQLite |
| `src/export.py` | Génération du fichier JSON lisible |
| `main.py` | Orchestration du pipeline complet |

## Modèle de données

**Table `destinations`**
- id, ville, pays, latitude, longitude

**Table `observations`**
- id, destination_id, temperature, humidite, precipitation, vent, code_meteo, date_observation

## Points d’extension

- Remplacement de SQLite par PostgreSQL
- Ajout d’un ordonnanceur (Airflow, cron)
- Conteneurisation avec Docker
- Exposition via une API interne
