# Pipeline météo pour le tourisme

> Collecte automatique de données météo via API publique, nettoyage et stockage SQL pour une entreprise touristique.

**Statut** : 🟢 Réalisé  
**Catégorie** : 📥 Système de collecte et de stockage  
**Portfolio** : [Profil GitHub](https://github.com/ousmajalloh405-eng)

---

## Problème métier

Une entreprise du secteur tourisme souhaite automatiser la collecte de données météo sur ses destinations afin d’optimiser les recommandations proposées aux clients (application mobile, site web).

## Architecture ETL

```
extract.py  →  transform.py  →  load.py
   (API)         (nettoyage)      (SQLite)
```

## Technologies

- Python 3
- `requests` (appel API)
- SQLite (stockage relationnel)
- API Open-Meteo (gratuite, sans clé API)

## Destinations suivies

Dakar, Paris, New York, Tokyo, Marrakech

## Installation

```bash
git clone https://github.com/ousmajalloh405-eng/meteo-tourisme.git
cd meteo-tourisme
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Exécution

```bash
python3 main.py
```

Le pipeline :
1. Crée la base `data/meteo.db`
2. Insère les destinations
3. Interroge l’API pour chaque ville
4. Nettoie les données
5. Insère les observations
6. Affiche un résumé

## Structure de la base

- `destinations` : ville, pays, coordonnées
- `observations` : température, humidité, précipitations, vent, date

## Notions travaillées

- Appel d’API REST (JSON)
- Pipeline ETL (Extract – Transform – Load)
- Gestion des valeurs manquantes
- Modélisation relationnelle simple
- Index SQL
- Organisation de projet Python

## Évolutions possibles

- Passage à PostgreSQL
- Conteneurisation Docker
- Orchestration avec Airflow (planification quotidienne)
- Ajout de prévisions sur plusieurs jours
- API interne pour l’application mobile

## Compétences pour le CV

Développement d’un pipeline ETL Python collectant des données météo via API publique, avec nettoyage et stockage dans une base relationnelle.

---

*Projet réalisé dans le cadre de la formation Data — Sonatel Academy.*
