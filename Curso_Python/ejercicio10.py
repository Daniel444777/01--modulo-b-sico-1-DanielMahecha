# ejercicio10.py - Manejo de Errores

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

while True:
    try:
        print("\n=== DIVISIÓN SEGURA ===")
        num1 = float(input("Numerador: "))
        num2 = float(input("Denominador: "))
        
        resultado = dividir(num1, num2)
        print(f"Resultado: {resultado}")
        break # Salir del bucle si todo sale bien

    except ValueError as e:
        print(f"Error: {e}. Intenta de nuevo.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")