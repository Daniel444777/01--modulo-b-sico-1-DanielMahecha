# main.py
from productos import GestorProductos
from carrito import Carrito
from ventas import Venta

# Inicializar los componentes principales
gestor_productos = GestorProductos()
carrito_actual = Carrito()

def mostrar_menu():
    print("\n" + "="*40)
    print("      SISTEMA DE GESTIÓN DE VENTAS")
    print("="*40)
    print("1. Mostrar Productos Disponibles")
    print("2. Agregar Producto al Carrito")
    print("3. Ver Carrito y Total")
    print("4. Procesar Compra (Pagar)")
    print("5. Salir")
    print("="*40)

def ejecutar_opcion(opcion):
    if opcion == '1':
        print("\n--- PRODUCTOS EN STOCK ---")
        for i, p in enumerate(gestor_productos.obtener_todos(), 1):
            print(f"{i}. {p}")
    
    elif opcion == '2':
        # Mostrar productos para que el usuario pueda elegir
        productos = gestor_productos.obtener_todos()
        for i, p in enumerate(productos, 1):
            print(f"{i}. {p.nombre}")

        try:
            indice = int(input("Selecciona el número del producto a comprar: ")) - 1
            cantidad = int(input("Ingresa la cantidad: "))
            
            if 0 <= indice < len(productos) and cantidad > 0:
                producto_seleccionado = productos[indice]
                carrito_actual.agregar_item(producto_seleccionado, cantidad)
            else:
                print("Selección o cantidad inválida.")

        except ValueError:
            print("Entrada inválida. Debe ser un número.")

    elif opcion == '3':
        carrito_actual.mostrar_detalle()
        
    elif opcion == '4':
        if not carrito_actual.items:
            print("ERROR: El carrito está vacío. Agrega productos primero.")
            return

        carrito_actual.mostrar_detalle()
        confirmacion = input("¿Confirmar y procesar la venta? (s/n): ").lower()
        
        if confirmacion == 's':
            venta = Venta(carrito_actual, gestor_productos)
            venta.procesar_venta()
            # Reiniciar el carrito para la próxima venta
            global carrito_actual
            carrito_actual = Carrito() 
        else:
            print("Venta cancelada.")
            
    elif opcion == '5':
        print("Gracias por usar el Sistema de Ventas. ¡Hasta pronto!")
        return True # Indica que se debe salir del bucle
        
    else:
        print("Opción no válida. Intenta de nuevo.")

# Bucle principal de la aplicación
def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")
        if ejecutar_opcion(opcion):
            break

if __name__ == "__main__":
    main()