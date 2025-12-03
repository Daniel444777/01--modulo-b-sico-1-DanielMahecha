# ejercicio8.py - Funciones

def saludar_persona(nombre, saludo="Hola"):
    """Función que saluda a una persona"""
    return f"{saludo}, {nombre}!"

def calcular_promedio(*numeros):
    """Calcula el promedio de cualquier cantidad de números"""
    return sum(numeros) / len(numeros)

# Usando las funciones
print(saludar_persona("Carlos"))
print(saludar_persona("Ana", "Buenos días"))

promedio = calcular_promedio(10, 20, 30, 40)
print(f"El promedio es: {promedio}")