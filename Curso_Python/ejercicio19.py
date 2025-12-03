# ejercicio19.py - Web Scraping Básico
# Requiere: pip install beautifulsoup4 requests
import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup(respuesta.text, 'html.parser')
    
    # Extraer el título de la página
    titulo = soup.title.string
    print(f"Título de la página: {titulo}")
    
    # Buscar botones o enlaces importantes
    boton = soup.find('a', class_='button')
    if boton:
        print(f"Texto del botón principal: {boton.text.strip()}")
else:
    print("No se pudo acceder a la página")