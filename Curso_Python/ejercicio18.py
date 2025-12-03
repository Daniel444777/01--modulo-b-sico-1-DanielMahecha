# ejercicio18.py - Automatización
# Requiere: pip install schedule
import schedule
import time

def tarea():
    print("Ejecutando tarea automática... ¡Hola!")

# Programar la tarea cada 3 segundos (para prueba rápida)
schedule.every(3).seconds.do(tarea)

print("Iniciando automatización (Presiona Ctrl+C para detener)...")

# Bucle infinito para mantener el script corriendo
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nAutomatización detenida.")