# ejercicio15.py - Base de Datos SQLite
import sqlite3

# 1. Conectar (crea el archivo si no existe)
conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

# 2. Crear una tabla
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER
    )
''')

# 3. Insertar datos
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Ana', 30)")
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Pedro', 25)")
conexion.commit() # Guardar cambios

# 4. Leer datos
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

print("--- USUARIOS EN BASE DE DATOS ---")
for usuario in usuarios:
    print(usuario)

conexion.close()