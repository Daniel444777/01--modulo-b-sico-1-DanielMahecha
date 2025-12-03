# ejercicio13.py - Expresiones Regulares
import re

texto = "Contactar a soporte@email.com o ventas@empresa.org para más info."

# Patrón para encontrar emails
patron_email = r'[\w\.-]+@[\w\.-]+\.\w+'

# Buscar todos los emails en el texto
emails_encontrados = re.findall(patron_email, texto)

print("Texto original:", texto)
print("Emails encontrados:", emails_encontrados)

# Validar un teléfono simple (10 dígitos)
telefono = "1234567890"
if re.match(r'^\d{10}$', telefono):
    print(f"El teléfono {telefono} es válido.")
else:
    print(f"El teléfono {telefono} no es válido.")