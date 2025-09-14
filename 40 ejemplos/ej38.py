import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analizar_csv(ruta_archivo):
    
    df = pd.read_csv(ruta_archivo)
    print("\n=== Datos cargados ===")
    print(df.head())


    print("\n=== Información del DataFrame ===")
    print(df.info())

    print("\n=== Estadísticas descriptivas ===")
    print(df.describe())


    for col in df.select_dtypes(include='number').columns:
        print(f"\n--- Estadísticas para {col} ---")
        print(f"Media: {df[col].mean()}")
        print(f"Mediana: {df[col].median()}")
        print(f"Moda: {df[col].mode().values}")
        print(f"Desviación estándar: {df[col].std()}")


    print("\nGenerando gráficos...")


    for col in df.select_dtypes(include='number').columns:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col], kde=True, bins=20)
        plt.title(f'Histograma de {col}')
        plt.xlabel(col)
        plt.ylabel('Frecuencia')
        plt.show()


    for col in df.select_dtypes(include='object').columns:
        plt.figure(figsize=(8, 4))
        df[col].value_counts().plot(kind='bar')
        plt.title(f'Frecuencia de {col}')
        plt.xlabel(col)
        plt.ylabel('Frecuencia')
        plt.show()

if __name__ == "__main__":
    ruta = input("Ingresa la ruta del archivo CSV: ")
    analizar_csv(ruta)
