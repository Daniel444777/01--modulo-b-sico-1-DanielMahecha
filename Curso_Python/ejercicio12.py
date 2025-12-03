# ejercicio12.py - Módulos y Paquetes
import math
import datetime

# Usando el módulo math
numero = 16
raiz = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es {raiz}")

# Usando el módulo datetime
ahora = datetime.datetime.now()
print(f"Fecha y hora actual: {ahora}")
print(f"Año actual: {ahora.year}")

# Ejemplo de función utilitaria
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

print(f"Área de un círculo de radio 5: {calcular_area_circulo(5):.2f}")