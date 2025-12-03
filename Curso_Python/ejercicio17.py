# ejercicio17.py - Visualización
# Requiere: pip install matplotlib
import matplotlib.pyplot as plt

meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May']
ventas = [1500, 2300, 1800, 2600, 3000]

plt.figure(figsize=(8, 5))
plt.bar(meses, ventas, color='skyblue')

plt.title('Ventas Mensuales')
plt.xlabel('Meses')
plt.ylabel('Dinero ($)')

print("Generando gráfico...")
plt.show() # Abre una ventana con el gráfico