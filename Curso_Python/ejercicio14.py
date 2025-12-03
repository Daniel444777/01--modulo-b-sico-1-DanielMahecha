# ejercicio14.py - Consumo de APIs
# Requiere: pip install requests
import requests

print("Consultando datos de internet...")

# Usamos una API pública de prueba
url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)

if response.status_code == 200:
    datos = response.json()
    print("Datos descargados con éxito:")
    print(f"Nombre: {datos['name']}")
    print(f"Email: {datos['email']}")
    print(f"Ciudad: {datos['address']['city']}")
else:
    print("Hubo un error al conectar con la API")