# ejercicio3.py - Entrada de datos

print("=== PROGRAMA INTERACTIVO ===")
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")

# Convertimos la entrada a números (float para decimales, int para enteros)
altura = float(input("¿Cuál es tu altura en metros? (ej: 1.75): "))
peso = float(input("¿Cuál es tu peso en kg?: "))

imc = peso / (altura ** 2)

print("\n" + "="*30)
print(f"Hola {nombre} {apellido}")
print(f"Tu índice de masa corporal es: {round(imc, 2)}")