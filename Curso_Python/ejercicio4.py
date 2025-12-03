# ejercicio4.py - Sistema de decisiones

print("SISTEMA DE CALIFICACIONES")
nota = float(input("Ingresa tu calificación (0-100): "))

if nota >= 90:
    print("¡Excelente! Calificación: A")
elif nota >= 80:
    print("Muy bien. Calificación: B")
elif nota >= 70:
    print("Bien. Calificación: C")
elif nota >= 60:
    print("Suficiente. Calificación: D")
else:
    print("Necesitas mejorar. Calificación: F")

# Condición anidada de ejemplo
if nota >= 60:
    print("Has APROBADO el curso.")
else:
    print("Has REPROBADO el curso.")