import tkinter as tk
from tkinter import font
from entidades.Autor import Autor
from controladores import ControladorAutor as c_a

# Función para capturar los datos y enviarlos al controlador
def enviar_datos():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    nacionalidad = entry_nacionalidad.get()
    
    if nombre and apellido and nacionalidad:
        autor = Autor(nombre, apellido, nacionalidad)
        c_a.guardar_autor(autor)
        limpiar_campos()  # Limpiar los campos después de enviar
        lbl_validacion.config(text="Autor registrado correctamente.", fg="Green")    
    else:
        lbl_validacion.config(text="Error: Complete todos los campos", fg="Red")    

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_nacionalidad.delete(0, tk.END)

# Función para cerrar la ventana
def salir():
    ventana.destroy()

def iniciar_ventana():
    global entry_nombre, entry_apellido, entry_nacionalidad, ventana, lbl_validacion

    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Formulario de Registro de Autor")
    ventana.geometry("500x400")  # Ancho de 500 píxeles y alto de 400 píxeles
    ventana.configure(bg="#F0F4F8")  # Fondo más suave

    # Estilos
    fuente_titulo = font.Font(family="Helvetica", size=16, weight="bold")
    fuente_label = font.Font(family="Arial", size=11)
    fuente_entry = font.Font(family="Arial", size=10)

    # Frame para el contenido con mayor espacio y borde redondeado
    frame = tk.Frame(ventana, padx=20, pady=20, bg="#FFFFFF", relief="solid", bd=2)
    frame.pack(pady=20, padx=10, fill="both", expand=True)

    # Título
    label_titulo = tk.Label(frame, text="Registrar Autor", font=fuente_titulo, bg="#FFFFFF", fg="#333333")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # Nombre
    tk.Label(frame, text="Nombre:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=1, column=0, sticky="e", padx=10, pady=8)
    entry_nombre = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_nombre.grid(row=1, column=1, pady=8)

    # Apellido
    tk.Label(frame, text="Apellido:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=2, column=0, sticky="e", padx=10, pady=8)
    entry_apellido = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_apellido.grid(row=2, column=1, pady=8)

    # Nacionalidad
    tk.Label(frame, text="Nacionalidad:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=3, column=0, sticky="e", padx=10, pady=8)
    entry_nacionalidad = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_nacionalidad.grid(row=3, column=1, pady=8)

    # Botón enviar
    boton_enviar = tk.Button(frame, text="Enviar", command=enviar_datos,
                             bg="#4CAF50", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_enviar.grid(row=4, column=0, columnspan=2, pady=10)
     
     # Etiquetas de validacion
    lbl_validacion = tk.Label(frame, text="", font=fuente_label, bg="#FFFFFF", fg="red")
    lbl_validacion.grid(row=6, column=0, columnspan=2, pady=10)

    # Botón salir
    boton_salir = tk.Button(frame, text="Salir", command=salir, bg="#f44336", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_salir.grid(row=5, column=0, columnspan=2, pady=10)
    
    

    ventana.mainloop()
