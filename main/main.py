import tkinter as tk
from tkinter import messagebox

class ClienteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Clientes")

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.usuario_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Usuario", menu=self.usuario_menu)
        self.usuario_menu.add_command(label="Registrar Usuario", command=self.registrar_usuario)
        self.usuario_menu.add_command(label="Mostrar Usuarios", command=self.mostrar_usuarios)
        self.usuario_menu.add_command(label="Modificar Usuario", command=self.modificar_usuario)

        self.historial_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Historial", menu=self.historial_menu)
        self.historial_menu.add_command(label="Historial de Cliente", command=self.historial_cliente)
        self.historial_menu.add_command(label="Historial General", command=self.historial_general)

        self.comprobante_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Comprobante", menu=self.comprobante_menu)
        self.comprobante_menu.add_command(label="Generar Comprobante", command=self.generar_comprobante)
        self.comprobante_menu.add_command(label="Confirmacion Pago", command=self.confirmacion_pago)

        self.deudas_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Deudas", menu=self.deudas_menu)
        self.deudas_menu.add_command(label="Deudas Pendientes", command=self.deudas_pendientes)
        self.deudas_menu.add_command(label="Calcular Pagos", command=self.calcular_pagos)

        self.menu.add_command(label="Admin", command=self.admin)
        self.menu.add_command(label="Herramientas M5", command=self.herramientas_m5)
        self.menu.add_command(label="Developer", command=self.developer)

    def registrar_usuario(self):
        messagebox.showinfo("Registrar Usuario", "Funcionalidad para registrar un usuario.")

    def mostrar_usuarios(self):
        messagebox.showinfo("Mostrar Usuarios", "Funcionalidad para mostrar usuarios.")

    def modificar_usuario(self):
        messagebox.showinfo("Modificar Usuario", "Funcionalidad para modificar un usuario.")

    def historial_cliente(self):
        messagebox.showinfo("Historial de Cliente", "Funcionalidad para mostrar historial de cliente.")

    def historial_general(self):
        messagebox.showinfo("Historial General", "Funcionalidad para mostrar historial general.")

    def generar_comprobante(self):
        messagebox.showinfo("Generar Comprobante", "Funcionalidad para generar un comprobante.")

    def confirmacion_pago(self):
        messagebox.showinfo("Confirmacion Pago", "Funcionalidad para confirmar un pago.")

    def deudas_pendientes(self):
        messagebox.showinfo("Deudas Pendientes", "Funcionalidad para mostrar deudas pendientes.")

    def calcular_pagos(self):
        messagebox.showinfo("Calcular Pagos", "Funcionalidad para calcular pagos.")

    def admin(self):
        messagebox.showinfo("Admin", "Funcionalidad para administrar.")

    def herramientas_m5(self):
        messagebox.showinfo("Herramientas M5", "Funcionalidad para herramientas M5.")

    def developer(self):
        messagebox.showinfo("Developer", "Funcionalidad para desarrollador.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ClienteApp(root)
    root.mainloop()
