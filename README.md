# Pipeline météo pour le tourisme

> Collecte automatique de données météo via API publique, nettoyage et stockage SQL pour une entreprise touristique.

**Statut** : 🟢 Réalisé  
**Catégorie** : 📥 Système de collecte et de stockage  
**Portfolio** : [Profil GitHub](https://github.com/ousmajalloh405-eng)

---

## 1. Problème métier

Une entreprise du secteur tourisme veut automatiser la collecte de données météo sur ses destinations afin d’améliorer les recommandations proposées aux clients (application mobile, site web).

## 2. Architecture

```
                    PIPELINE ETL
                         │
         ┌──────────────┴─────────────┐
         ▼               ▼               ▼
    extract.py     transform.py      load.py
   (API REST)      (nettoyage)      (SQLite)
         │               │               │
         └──────────────┴─────────────┘
                         │
                    data/meteo.db
                         +
                 data/meteo_export.json
```

**Flux** :
1. `extract.py` interroge l’API Open-Meteo
2. `transform.py` nettoie et normalise les données
3. `load.py` insère dans SQLite
4. Un export JSON lisible est généré automatiquement

## 3. Structure du projet

```
meteo-tourisme/
├── src/
│   ├── config.py       # Liste des destinations
│   ├── extract.py      # Appel API
│   ├── transform.py    # Nettoyage
│   ├── load.py         # Insertion SQLite
│   └── export.py       # Export JSON
├── data/
│   ├── meteo.db        # Base SQLite
│   └── meteo_export.json
├── main.py             # Orchestration
├── requirements.txt
└── README.md
```

## 4. Technologies

| Composant | Technologie |
|-----------|-------------|
| Langage | Python 3 |
| API | Open-Meteo (gratuite, sans clé) |
| Stockage | SQLite |
| Format lisible | JSON |

## 5. Installation et exécution

```bash
git clone https://github.com/ousmajalloh405-eng/meteo-tourisme.git
cd meteo-tourisme
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## 6. Résultats

Après exécution :
- Base `data/meteo.db` alimentée
- Fichier `data/meteo_export.json` lisible
- Affichage des températures des 5 destinations

## 7. Compétences pour le CV

Développement d’un pipeline ETL Python collectant des données météo via API publique, avec nettoyage, stockage relationnel et export JSON.

---

*Projet réalisé dans le cadre de la formation Data — Sonatel Academy.*
