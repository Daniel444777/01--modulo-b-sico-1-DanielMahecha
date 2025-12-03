# ejercicio21.py - Machine Learning Simple
# Requiere: pip install scikit-learn
from sklearn.linear_model import LinearRegression
import numpy as np

# Datos: [Metros Cuadrados] -> [Precio en miles]
X = np.array([[50], [60], [80], [100]]) # Entrada (Feature)
y = np.array([150, 180, 240, 300])      # Salida (Label)

# Entrenar modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predecir precio para una casa de 120 mts
nuevo_dato = np.array([[120]])
prediccion = modelo.predict(nuevo_dato)

print("Modelo entrenado.")
print(f"Predicción precio casa 120m2: ${prediccion[0]:.2f} miles")