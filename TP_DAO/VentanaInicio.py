import tkinter as tk
from tkinter import font
import VentanaRegAutor as v_a
import VentanaRegistrarLibro as v_l

# Función para salir de la aplicación
def salir_aplicacion():
    print("Cerrando la aplicación...")
    ventana_inicio.destroy()
    exit()
    

def iniciar_ventana_inicio():
    global ventana_inicio
    ventana_inicio = tk.Tk()
    ventana_inicio.title("Sistema de Gestión de libreria")
    ventana_inicio.geometry("400x300")

    # Estilos
    fuente_titulo = font.Font(family="Helvetica", size=16, weight="bold")
    fuente_botones = font.Font(family="Helvetica", size=12)

    # Título
    label_titulo = tk.Label(ventana_inicio, text="Bienvenido al Sistema de Gestión", font=fuente_titulo, pady=20)
    label_titulo.pack()

    # Botón para registrar autores
    boton_registrar_autor = tk.Button(
        ventana_inicio, 
        text="Registrar Autores", 
        command=v_a.iniciar_ventana, 
        bg="#1E88E5", 
        fg="white", 
        padx=20, 
        pady=10, 
        font=fuente_botones
    )
    boton_registrar_autor.pack(pady=10)
    
    # Botón para registrar libros
    boton_registrar_autor = tk.Button(
        ventana_inicio, 
        text="Registrar Libros", 
        command=v_l.iniciar_ventana, 
        bg="#1E88E5", 
        fg="white", 
        padx=20, 
        pady=10, 
        font=fuente_botones
    )
    boton_registrar_autor.pack(pady=10)

    # Botón para salir
    boton_salir = tk.Button(
        ventana_inicio, 
        text="Salir", 
        command=salir_aplicacion, 
        bg="#F44336", 
        fg="white", 
        padx=20, 
        pady=10, 
        font=fuente_botones
    )
    boton_salir.pack(pady=10)

    ventana_inicio.mainloop()
