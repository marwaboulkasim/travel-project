import pandas as pd
from clean_data import load_and_clean_data

def print_statistics(df: pd.DataFrame) -> None:
    print("=== Distribution des valeurs météo ===")
    print(df['weather'].value_counts(dropna=False))
    print()

    print("=== Distribution des humeurs ===")
    print(df['mood'].value_counts(dropna=False))
    print()

    print("=== Statistiques descriptives sur 'photos' ===")
    mean_photos = df['photos'].mean()
    median_photos = df['photos'].median()
    min_photos = df['photos'].min()
    max_photos = df['photos'].max()
    print(f"Moyenne : {mean_photos:.2f}")
    print(f"Médiane : {median_photos}")
    print(f"Minimum : {min_photos}")
    print(f"Maximum : {max_photos}")
    print()

    print("=== Valeurs manquantes détectées ===")
    missing_values = df.isnull().sum().sum()
    print(f"Total valeurs manquantes dans le DataFrame : {missing_values}")
    print()

    print("=== Valeurs aberrantes détectées dans 'photos' ===")
    aberrant_photos = (df['photos'] < 0).sum()
    print(f"Nombre de valeurs négatives dans 'photos' : {aberrant_photos}")

if __name__ == "__main__":
    df = load_and_clean_data("travel_data.csv")
    print_statistics(df)
