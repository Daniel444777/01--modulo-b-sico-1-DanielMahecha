# ejercicio6.py - Bucles For

print("=== TABLA DEL 5 ===")
for i in range(1, 11):
    resultado = 5 * i
    print(f"5 x {i} = {resultado}")

print("\n=== RECORRIENDO LISTA ===")
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores, start=1):
    print(f"{indice}. Color: {color}")