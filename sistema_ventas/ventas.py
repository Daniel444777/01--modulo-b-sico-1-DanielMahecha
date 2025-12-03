# ventas.py
from datetime import datetime
from pathlib import Path

class Venta:
    """Clase para representar y registrar la transacción final."""
    def __init__(self, carrito, gestor_productos):
        self.carrito = carrito
        self.gestor_productos = gestor_productos
        self.fecha = datetime.now()
        self.total = carrito.calcular_total()

    def procesar_venta(self):
        """Ejecuta la venta, actualiza el stock y genera el log."""
        
        # 1. Actualizar stock y preparar log
        lineas_log = []
        for producto, cantidad in self.carrito.items.items():
            self.gestor_productos.actualizar_stock(producto, cantidad)
            lineas_log.append(f"  - {producto.nombre} | Cant: {cantidad} | Total: {producto.precio * cantidad:.2f}")

        # 2. Generar registro de venta
        log_venta = (
            f"VENTA REALIZADA: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"TOTAL FINAL: ${self.total:.2f}\n"
            f"ITEMS:\n"
            + "\n".join(lineas_log) + "\n"
            + "="*40 + "\n"
        )
        
        # 3. Guardar el log en un archivo
        log_file = Path("data/registro_ventas.log")
        log_file.parent.mkdir(parents=True, exist_ok=True)
        with open(log_file, 'a') as f:
            f.write(log_venta)

        print("\n*** VENTA PROCESADA CON ÉXITO ***")
        print(f"Registro guardado en {log_file}")
        print(f"Stock de productos actualizado.")