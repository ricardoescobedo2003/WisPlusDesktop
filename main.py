import tkinter as tk
from tkinter import Menu

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana con Menú Desplegable")
root.geometry("400x300")

# Funciones para los comandos del menú
def nuevo_archivo():
    print("Nuevo archivo creado")

def abrir_archivo():
    print("Archivo abierto")

def guardar_archivo():
    print("Archivo guardado")

def salir():
    root.quit()

# Crear la barra de menú
menubar = Menu(root)

# Crear el menú de Archivo
archivo_menu = Menu(menubar, tearoff=0)
archivo_menu.add_command(label="Nuevo", command=nuevo_archivo)
archivo_menu.add_command(label="Abrir", command=abrir_archivo)
archivo_menu.add_command(label="Guardar", command=guardar_archivo)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir)

# Añadir el menú de Archivo a la barra de menú
menubar.add_cascade(label="Clientes", menu=archivo_menu)

# Mostrar la barra de menú en la ventana principal
root.config(menu=menubar)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
