# ejercicio7.py - Diccionarios

persona = {
    "nombre": "Ana García",
    "edad": 28,
    "ciudad": "Madrid",
    "profesion": "Ingeniera"
}

# Acceder y modificar
print(f"Nombre: {persona['nombre']}")
persona["telefono"] = "555-1234" # Agregar nuevo
persona["edad"] = 29 # Modificar existente

print("\n=== DATOS COMPLETOS ===")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")