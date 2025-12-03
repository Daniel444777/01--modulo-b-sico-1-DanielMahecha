# ejercicio5.py - Listas dinámicas

frutas = ["manzana", "banana", "naranja"]
print(f"Lista inicial: {frutas}")

# Agregar elementos
frutas.append("uva")
frutas.insert(1, "pera")
print(f"Después de agregar: {frutas}")

# Eliminar elementos
frutas.remove("banana")
ultimo = frutas.pop() # Elimina el último
print(f"Después de eliminar: {frutas}")
print(f"Fruta eliminada del final: {ultimo}")

# Ordenar
frutas.sort()
print(f"Lista ordenada alfabéticamente: {frutas}")