# ejercicio23.py - Interfaz Gráfica (GUI)
import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Saludo", "¡Hola! Has pulsado el botón.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mi App de Escritorio")
ventana.geometry("300x200")

# Agregar etiqueta
etiqueta = tk.Label(ventana, text="Bienvenido a Python GUI", font=("Arial", 12))
etiqueta.pack(pady=20)

# Agregar botón
boton = tk.Button(ventana, text="Púlsame", command=mostrar_mensaje)
boton.pack()

# Iniciar aplicación
ventana.mainloop()