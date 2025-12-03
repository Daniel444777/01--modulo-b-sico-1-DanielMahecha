# ejercicio16.py - Pandas DataFrames
# Requiere: pip install pandas
import pandas as pd

datos = {
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor"],
    "Precio": [800, 20, 50, 200],
    "Stock": [10, 50, 30, 15]
}

df = pd.DataFrame(datos)

print("--- DATAFRAME DE PRODUCTOS ---")
print(df)

# Análisis simple
print("\nEstadísticas:")
print(f"Precio promedio: ${df['Precio'].mean()}")
print(f"Total de stock: {df['Stock'].sum()}")

# Guardar a CSV
df.to_csv("reporte_productos.csv", index=False)
print("\nArchivo 'reporte_productos.csv' guardado.")