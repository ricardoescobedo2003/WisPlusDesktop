import tkinter as tk
from tkinter import Menu
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Wisplus Desktop")
root.geometry("900x600")
#hola
# Funciones para los comandos del menú
def ver_cliente():
    print("Nuevo archivo creado")

def crear_cliente():
    # Crear una nueva ventana (Toplevel) para ingresar datos del cliente
    ventana_cliente = Toplevel(root)
    ventana_cliente.title("Crear Cliente")
    ventana_cliente.geometry("400x300")

    # Función para guardar los datos del cliente
    def guardar_cliente():
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()

        # Aquí puedes guardar los datos del cliente en una base de datos o realizar otras acciones
        print(f"Cliente creado: {nombre}, {direccion}, {telefono}")
        messagebox.showinfo("Cliente Creado", f"Cliente {nombre} creado exitosamente")

        # Cerrar la ventana después de guardar
        ventana_cliente.destroy()

    # Crear etiquetas y campos de entrada para los datos del cliente
    tk.Label(ventana_cliente, text="Nombre:").pack()
    entry_nombre = tk.Entry(ventana_cliente)
    entry_nombre.pack()

    tk.Label(ventana_cliente, text="Dirección:").pack()
    entry_direccion = tk.Entry(ventana_cliente)
    entry_direccion.pack()

    tk.Label(ventana_cliente, text="Teléfono:").pack()
    entry_telefono = tk.Entry(ventana_cliente)
    entry_telefono.pack()

    # Botón para guardar los datos del cliente
    tk.Button(ventana_cliente, text="Guardar Cliente", command=guardar_cliente).pack(pady=20)

def actualizar_cliente():
    print("Archivo guardado")

def eliminar_cliente():
    print("Clientes eliminados")

def ver_pagos():
    pass
def crear_pago():
    pass
def buscar_pago():
    pass
def crear_comprobante():
    pass

def salir():
    aks = messagebox.askokcancel("Salir?", "Estas seguro?, se detendran los cortes automaticos")
    if aks:
        root.quit()
    else:
        print("Uff que susto")

def corteHoras():
    pass
def cortePorDias():
    pass
def cortePorFechas():
    pass
def cortePorSemana():
    pass
def corteAutomatico():
    pass


def infoAntena():
    pass
def reiniciarAntena():
    pass
def bloquearAntena():
    pass
def desbloquearAntena():
    pass
    
def about():
    messagebox.showinfo("Información", "Este es un mensaje de información")
# Crear la barra de menú
menubar = Menu(root)

# Crear el menú de Archivo #CRUD
archivo_menu = Menu(menubar, tearoff=0)
archivo_menu.add_command(label="Ver Cliente", command=ver_cliente)
archivo_menu.add_command(label="Crear Cliente", command=crear_cliente)
archivo_menu.add_command(label="Actualizar Cliente", command=actualizar_cliente)
archivo_menu.add_command(label="Eliminar Cliente", command=eliminar_cliente)
#archivo_menu.add_separator()


# Crear el menú de Archivo #CRUD
pagos_menu = Menu(menubar, tearoff=0)
pagos_menu.add_command(label="Ver Pagos", command=ver_pagos)
pagos_menu.add_command(label="Crear Pago", command=crear_pago)
pagos_menu.add_command(label="Buscar Pagos", command=buscar_pago)
pagos_menu.add_command(label="Crear Comprobante", command=crear_comprobante)


#Menu de automatizacion
automatizacion_menu = Menu(menubar, tearoff=0)
automatizacion_menu.add_command(label="Corte por Horas", command=corteHoras)
automatizacion_menu.add_command(label="Corte por Dias", command=cortePorDias)
automatizacion_menu.add_command(label="Corte por Semana", command=cortePorSemana)
automatizacion_menu.add_command(label="Corte por Fecha", command=cortePorFechas)
automatizacion_menu.add_command(label="Corte Automatico", command=corteAutomatico)

m5 = Menu(menubar, tearoff=0)
m5.add_command(label="Info Anten", command=infoAntena)
m5.add_command(label="Reiniciar Antena", command=reiniciarAntena)
m5.add_command(label="Bloquear Antena", command=bloquearAntena)
m5.add_command(label="Desbloquear Antena", command=desbloquearAntena)

about = Menu(menubar, tearoff=0)
about.add_command(label="Informacion", command=about)

salir_menu = Menu(menubar, tearoff=0)
salir_menu.add_command(label="Salir", command=salir)

# Añadir el menú de Archivo a la barra de menú
menubar.add_cascade(label="Clientes", menu=archivo_menu)
menubar.add_cascade(label="Pagos", menu=pagos_menu)
menubar.add_cascade(label="Automatizar", menu=automatizacion_menu)
menubar.add_cascade(label="Herramientas M5", menu=m5)
menubar.add_cascade(label="About", menu=about)
menubar.add_cascade(label="Quit", menu=salir_menu)
# Mostrar la barra de menú en la ventana principal
root.config(menu=menubar)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
