# Mini-application Python pour les analyser les données de voyage

## Contexte

Maintenant que vous avez fait les notebooks pour découvrir les différentes étapes de traitement de données, vous allez créer une petite application complète qui permet de :

- Charger et nettoyer un jeu de données 
- Afficher des statistiques descriptives sur les données nettoyées
- Réaliser des visualisations simples pour mieux comprendre les données



## Jeu de données utilisé

Le fichier `travel_data.csv` contient un carnet de voyage avec les colonnes suivantes :

- `city` : nom de la ville (française)
- `date` : date de la visite
- `weather` : conditions météo (sunny, cloudy, rainy, snowy)
- `mood` : humeur associée
- `photos` : nombre de photos prises

---

## Liste des fichiers à coder

### 1. `clean_data.py`

- Fonction `load_and_clean_data(filename: str) -> pd.DataFrame`  
  - Charger le fichier CSV  
  - Traiter les valeurs manquantes, justifier le choix fait pour le traitement 
  - Détecter et traiter les valeurs aberrantes, justifier les choix faits
  - Retourner un DataFrame propre et prêt à l’analyse

### 2. `print_stat.py`

- Fonction `print_statistics(df: pd.DataFrame) -> None`  
  - Afficher la distribution des valeurs météo et humeur  
  - Afficher des statistiques descriptives sur la colonne `photos` (moyenne, médiane, min, max)  
  - Afficher le nombre de valeurs manquantes et aberrantes détectées

### 3. `plot_data.py`

- Fonction `plot_photos_by_weather(df: pd.DataFrame) -> None`  
  - Créer un graphique montrant le nombre moyen de photos prises par condition météo  
- Fonction `plot_mood_distribution(df: pd.DataFrame) -> None`  
  - Visualiser la répartition des humeurs dans les données  
- Fonction pour visualiser l’évolution des photos prises au fil du temps

### 4. `main.py`

- Script principal qui :  
  - Importe et utilise les fonctions des modules précédents  
  - Charge et nettoie les données  
  - Affiche les statistiques  
  - Produit les graphiques  
  - Permet une exécution simple et claire du projet

---

## Ressources

- Documentation pandas : https://pandas.pydata.org/pandas-docs/stable/  
- Documentation plotly :  https://plotly.com/python/
- Notebooks des phases précédentes pour des exemples de code
- Comprendre l'utilisation du script `main`: https://realpython.com/python-main-function/

---

## Instructions

- Travaillez d’abord sur chaque fichier séparément
- Organisez bien votre code et commentez-le clairement 
- Pour importer des fonctions d'un fichier différent utiliser par exemple `from plot_data import plot_photos_by_weather`
- Le script `main.py` doit être le point d’entrée unique pour lancer toute l’application, vous aider de la ressource pour comprendre et écrire le script.
- Dans le terminal, le code doit se lancer quand vous taper : `python3 main.py`

**Bonus du bonus**
- Ajouter un script `add_data.py` qui permet de demander à l'utilisateur d'ajouter un nouveau voyage, en le guidant sur les champs à reneigner et les ajouter dans le fichier csv
- Ajouter cette fonctionnalité dans le main.py

- Chercher des outils permettant d'afficher des données sur une carte
- En fonction de l'outil choisi, y'a-t-il des données supplémentaires à récuppérer ?
- Implémenter dans `plot_data.py` une fonction pour visualiser les destinations sur une carte 

- Ajouter de la doc
- Ajouter des tests

- Imaginons que d'autres données soient disponibles dans une base de données. Quelles étapes faudrait-il ajouter pour les utiliser en plus du csv ?   
Quelles modifications pourraient être faites sur l'architecture du code pour anticiper l'ajout d'une autre source de données ? 
- Implémenter les solutions proposées

- Utiliser streamlit pour afficher vos graphes en vous appuyant sur la doc : https://streamlit.io/
- Ajouter une interface pour que les utilisateurs puissent choisir quelles variables afficher sur chaque axe d'un graphe. 




