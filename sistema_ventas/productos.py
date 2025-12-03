# productos.py
import json
from pathlib import Path

class Producto:
    """Clase para representar un producto en el sistema."""
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        # Método para mostrar el producto de forma legible
        return f"{self.nombre} (Precio: ${self.precio:.2f} | Stock: {self.stock})"

    def to_dict(self):
        # Convierte el objeto a diccionario para guardarlo en JSON
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }

class GestorProductos:
    """Maneja la carga y gestión de la lista de productos."""
    def __init__(self, archivo="data/productos.json"):
        self.archivo = Path(archivo)
        self.productos = []
        self._cargar_productos()

    def _cargar_productos(self):
        # Carga los productos desde el archivo JSON si existe
        if self.archivo.exists():
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                # Recrea objetos Producto desde el diccionario
                for d in datos:
                    self.productos.append(Producto(**d))
        else:
            # Productos por defecto si no hay archivo
            print("Creando productos iniciales...")
            self.productos.append(Producto("Laptop Dell", 850.00, 10))
            self.productos.append(Producto("Mouse Óptico", 15.50, 50))
            self.productos.append(Producto("Teclado Mecánico", 60.00, 25))

    def guardar_productos(self):
        # Guarda la lista actual de productos en el archivo JSON
        self.archivo.parent.mkdir(parents=True, exist_ok=True) # Crea la carpeta 'data'
        datos = [p.to_dict() for p in self.productos]
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def obtener_todos(self):
        # Retorna la lista de todos los productos
        return self.productos

    def buscar_por_nombre(self, nombre_buscado):
        # Busca un producto por nombre (exacto)
        for p in self.productos:
            if p.nombre.lower() == nombre_buscado.lower():
                return p
        return None

    def actualizar_stock(self, producto, cantidad):
        # Actualiza el stock después de una venta
        if producto in self.productos:
            producto.stock -= cantidad
            self.guardar_productos()
            return True
        return False