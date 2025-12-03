# carrito.py

class Carrito:
    """Clase para gestionar los productos seleccionados por el cliente."""
    def __init__(self):
        # El carrito se guarda como un diccionario: {Producto: cantidad}
        self.items = {} 

    def agregar_item(self, producto, cantidad):
        """Agrega un producto al carrito, manejando el stock."""
        if producto.stock >= cantidad:
            if producto in self.items:
                self.items[producto] += cantidad
            else:
                self.items[producto] = cantidad
            return True
        else:
            print(f"ERROR: Solo hay {producto.stock} unidades de {producto.nombre} disponibles.")
            return False

    def calcular_total(self):
        """Calcula el costo total de todos los items en el carrito."""
        total = 0
        for producto, cantidad in self.items.items():
            total += producto.precio * cantidad
        return total

    def mostrar_detalle(self):
        """Imprime el detalle de la compra."""
        print("\n--- DETALLE DEL CARRITO ---")
        for producto, cantidad in self.items.items():
            subtotal = producto.precio * cantidad
            print(f"- {producto.nombre} | Cantidad: {cantidad} | Subtotal: ${subtotal:.2f}")
        print(f"TOTAL A PAGAR: ${self.calcular_total():.2f}")
        print("---------------------------")