# ejercicio11.py - Clases y Objetos

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"{self.marca} {self.modelo} encendido.")

    def apagar(self):
        self.encendido = False
        print(f"{self.marca} {self.modelo} apagado.")

# Herencia: Auto hereda de Vehiculo
class Auto(Vehiculo):
    def tocar_bocina(self):
        print("¡Beeeep beeeep!")

# Probamos el código
mi_auto = Auto("Toyota", "Corolla")
mi_auto.encender()
mi_auto.tocar_bocina()
print(f"¿Está encendido? {mi_auto.encendido}")