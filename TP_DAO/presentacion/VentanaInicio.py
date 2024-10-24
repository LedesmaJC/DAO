import tkinter as tk
from tkinter import font
from presentacion import VentanaRegAutor as v_a
from presentacion import VentanaRegistrarLibro as v_l
from presentacion import VentanaRegUsuario as v_u
from presentacion import VentanaConsultaLibros as v_c
from presentacion import VentanaRegPrestamo as v_p


# Función para salir de la aplicación
def salir_aplicacion():
    print("Cerrando la aplicación...")
    ventana_inicio.destroy()
    exit()

def iniciar_ventana_inicio():
    global ventana_inicio
    ventana_inicio = tk.Tk()
    ventana_inicio.title("Sistema de Gestión de Librería")
    ventana_inicio.geometry("600x600")

    # Estilos
    fuente_titulo = font.Font(family="Helvetica", size=16, weight="bold")
    fuente_botones = font.Font(family="Helvetica", size=12)

    # Título
    label_titulo = tk.Label(ventana_inicio, text="Bienvenido al Sistema de Gestión", font=fuente_titulo, pady=20)
    label_titulo.grid(row=0, column=0, columnspan=2, pady=20)  # Centrar el título

    frame_botones = tk.Frame(ventana_inicio)
    frame_botones.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

    boton_registrar_autor = tk.Button(
        frame_botones,
        text="Registrar Autores",
        command=v_a.iniciar_ventana,
        bg="#1E88E5",
        fg="black",
        padx=20,
        pady=10,
        font=fuente_botones
    )
    boton_registrar_autor.grid(row=0, column=0, padx=10, pady=10)  

    boton_registrar_libro = tk.Button(
        frame_botones,
        text="Registrar Libros",
        command=v_l.iniciar_ventana,
        bg="#1E88E5",
        fg="black",
        padx=20,
        pady=10,
        font=fuente_botones
    )
    boton_registrar_libro.grid(row=0, column=1, padx=10, pady=10)  

    boton_consultar_libros = tk.Button(
        frame_botones,
        text="Consultar Libros",
        command=v_c.iniciar_ventana,
        bg="#1E88E5",
        fg="black",
        padx=20,
        pady=10,
        font=fuente_botones
    )
    boton_consultar_libros.grid(row=1, column=0, padx=10, pady=10)  

    boton_registrar_usuario = tk.Button(
        frame_botones,
        text="Registrar Usuario",
        command=v_u.iniciar_ventana,
        bg="#1E88E5",
        fg="black",
        padx=20,
        pady=10,
        font=fuente_botones
    )
    boton_registrar_usuario.grid(row=1, column=1, padx=10, pady=10) 
    
    boton_registrar_prestamo = tk.Button(
        frame_botones,
        text="Registrar Prestamo",
        command=v_p.iniciar_ventana_prestamo,
        bg="#1E88E5",
        fg="black",
        padx=20,
        pady=10,
        font=fuente_botones
    )
    boton_registrar_prestamo.grid(row=1, column=2, padx=10, pady=10)  
 

    # Botón para salir
    boton_salir = tk.Button(
        ventana_inicio,
        text="Salir",
        command=salir_aplicacion,
        bg="#F44336",
        fg="black",
        padx=20,
        pady=10,
        font=fuente_botones
    )
    boton_salir.grid(row=2, column=0, columnspan=2, pady=20)  

    ventana_inicio.mainloop()
