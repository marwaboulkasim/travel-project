import pandas as pd

def load_and_clean_data(filename: str) -> pd.DataFrame:
    # Chargement des données
    df = pd.read_csv("clean_travel_data.csv")

    print("Données brutes :")
    print(df.info())
    print(df.describe())

    # Nettoyage : valeurs manquantes
    df = df.dropna(subset=['weather'])

    # Nettoyage : valeurs aberrantes
    df['photos'] = df['photos'].apply(lambda x: x if x >= 0 else None)
    median_photos = df['photos'].median()
    df['photos'] = df['photos'].fillna(median_photos)

    df['date'] = pd.to_datetime(df['date'])

    return df



if __name__ == "__main__":
    df_cleaned = load_and_clean_data("travel_data.csv")
    print("\n✅ Données nettoyées :")
    print(df_cleaned)   # Affiche tout le contenu du DataFrame nettoyé dans la console.
