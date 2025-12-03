# ejercicio9.py - Manejo de Archivos
from pathlib import Path

# Crear y escribir en un archivo
archivo = Path("notas.txt")
archivo.write_text("Esta es mi primera nota guardada desde Python.\nSegunda línea de texto.")

print("Archivo 'notas.txt' creado correctamente.")

# Leer el archivo
if archivo.exists():
    contenido = archivo.read_text()
    print("\n--- CONTENIDO DEL ARCHIVO ---")
    print(contenido)