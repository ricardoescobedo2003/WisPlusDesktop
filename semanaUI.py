import tkinter as tk
from tkinter import ttk
import paramiko
import schedule
import time

def adjust_bandwidth(queue_name, new_max_limit, hostname, username, password):
    # Función para ajustar el ancho de banda
    port = 22  # Puerto SSH, generalmente es 22

    # Comando para ajustar el ancho de banda
    command = f'/queue simple set [find name="{queue_name}"] max-limit={new_max_limit}'

    # Crear una instancia del cliente SSH
    client = paramiko.SSHClient()

    # Agregar automáticamente la clave del servidor si no está en la lista de known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Conectarse al dispositivo
        client.connect(hostname, port, username, password)
        
        # Ejecutar el comando para ajustar el ancho de banda
        stdin, stdout, stderr = client.exec_command(command)
        
        # Leer y mostrar la salida del comando, si es necesario
        output = stdout.read().decode()
        errors = stderr.read().decode()
        
        if output:
            print(f"Output: {output}")
        if errors:
            print(f"Errors: {errors}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Cerrar la conexión
        client.close()

def run_scheduler():
    global hostname_entry, username_entry, password_entry, queue_name_entry
    global start_time_entry, first_limit_entry, end_time_entry, second_limit_entry

    # Obtener los valores de los campos
    hostname = hostname_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    queue_name = queue_name_entry.get()
    start_time = start_time_entry.get()
    first_limit = first_limit_entry.get()
    end_time = end_time_entry.get()
    second_limit = second_limit_entry.get()
    
    # Obtener los días seleccionados
    days = [day_var.get() for day_var in day_vars if day_var.get() == 1]

    # Programar tareas con schedule
    for day in days:
        schedule.every().__getattribute__(day).at(start_time).do(adjust_bandwidth, queue_name, first_limit, hostname, username, password)
        schedule.every().__getattribute__(day).at(end_time).do(adjust_bandwidth, queue_name, second_limit, hostname, username, password)

    print(f"Scheduler iniciado. Ejecutando ajustes de ancho de banda a las {start_time} y {end_time} los días {', '.join(days)}...")

    # Bucle infinito para mantener el script en ejecución y verificar el horario
    while True:
        schedule.run_pending()
        time.sleep(1)

# Crear ventana principal
root = tk.Tk()
root.title("Configuración de Ancho de Banda")

# Crear etiquetas y entradas para los datos
fields = [
    ("Hostname", "122.122.124.1"),
    ("Username", "admin"),
    ("Password", "070523"),
    ("Queue Name", "Madrina"),
    ("Start Time", "22:30"),
    ("First Limit", "1k/1k"),
    ("End Time", "06:00"),
    ("Second Limit", "100M/15M")
]

day_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_vars = []

# Definir las variables globales para las entradas
hostname_entry = None
username_entry = None
password_entry = None
queue_name_entry = None
start_time_entry = None
first_limit_entry = None
end_time_entry = None
second_limit_entry = None

# Crear etiquetas y entradas para los datos
for i, (label, default) in enumerate(fields):
    row = tk.Frame(root)
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    label = tk.Label(row, width=15, text=label, anchor='w')
    label.pack(side=tk.LEFT)
    entry = tk.Entry(row)
    entry.insert(0, default)
    entry.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
    
    if label.cget("text") == "Hostname":
        hostname_entry = entry
    elif label.cget("text") == "Username":
        username_entry = entry
    elif label.cget("text") == "Password":
        password_entry = entry
    elif label.cget("text") == "Queue Name":
        queue_name_entry = entry
    elif label.cget("text") == "Start Time":
        start_time_entry = entry
    elif label.cget("text") == "First Limit":
        first_limit_entry = entry
    elif label.cget("text") == "End Time":
        end_time_entry = entry
    elif label.cget("text") == "Second Limit":
        second_limit_entry = entry

# Días de la semana
days_frame = tk.Frame(root)
days_frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
for day_label in day_labels:
    day_var = tk.IntVar()
    day_check = tk.Checkbutton(days_frame, text=day_label, variable=day_var)
    day_check.pack(side=tk.LEFT, padx=5)
    day_vars.append(day_var)

# Botón para ejecutar el scheduler
run_button = tk.Button(root, text='Ejecutar Scheduler', command=run_scheduler)
run_button.pack(side=tk.TOP, pady=10)

root.mainloop()
