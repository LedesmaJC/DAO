import tkinter as tk
from tkinter import font
from Autor import Autor

def enviar_datos():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    nacionalidad = entry_nacionalidad.get()
    autor = Autor(nombre, apellido, nacionalidad)
    ventana.quit()  # Cierra la ventana al enviar
    return autor

def iniciar_ventana():
    global entry_nombre, entry_apellido, entry_nacionalidad, ventana

    ventana = tk.Tk()
    ventana.title("Formulario de Datos")
    ventana.geometry("300x200")  # Tamaño de la ventana

    # Estilos
    fuente_titulo = font.Font(family="Helvetica", size=14, weight="bold")
    fuente_label = font.Font(family="Helvetica", size=10)

    # Crear un frame para el contenido con padding
    frame = tk.Frame(ventana, padx=10, pady=10)
    frame.pack(expand=True)

    # Título
    label_titulo = tk.Label(frame, text="Registro de Autor", font=fuente_titulo)
    label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    # Nombre
    tk.Label(frame, text="Nombre:", font=fuente_label).grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_nombre = tk.Entry(frame)
    entry_nombre.grid(row=1, column=1, pady=5)

    # Apellido
    tk.Label(frame, text="Apellido:", font=fuente_label).grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entry_apellido = tk.Entry(frame)
    entry_apellido.grid(row=2, column=1, pady=5)

    # Nacionalidad
    tk.Label(frame, text="Nacionalidad:", font=fuente_label).grid(row=3, column=0, sticky="e", padx=5, pady=5)
    entry_nacionalidad = tk.Entry(frame)
    entry_nacionalidad.grid(row=3, column=1, pady=5)

    # Botón enviar
    boton_enviar = tk.Button(frame, text="Enviar", command=enviar_datos, bg="#4CAF50", fg="white", padx=10, pady=5)
    boton_enviar.grid(row=4, column=0, columnspan=2, pady=10)

    ventana.mainloop()

# Iniciar la ventana
iniciar_ventana()
