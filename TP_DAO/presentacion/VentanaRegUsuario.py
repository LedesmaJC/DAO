import tkinter as tk
from tkinter import font
from tkinter import ttk  # Para usar Combobox
from entidades.Usuario import Usuario
from controladores import ControladorUsuario as c_u  # Asegúrate de tener este controlador

# Función para enviar los datos del usuario
def enviar_datos():
    #user_id = entry_id.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    tipo = combobox_tipo.get()  # Obtener el tipo seleccionado
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()

    if  nombre and apellido and tipo and direccion and telefono:
        usuario = Usuario(nombre, apellido, tipo, direccion, telefono)

        try:
            c_u.guardar_usuario(usuario)
            limpiar_campos()  # Limpiar los campos después de enviar
            lbl_validacion.config(text="", fg="#333333")  # Limpiar mensaje de error
            lbl_validacion.config(text="Usuario registrado correctamente.", fg="green")
            print("Datos del usuario enviados correctamente.")
        except Exception as e:
            lbl_validacion.config(text=f"Error: {str(e)}", fg="red")  # Mostrar el mensaje de error
    else:
        lbl_validacion.config(text="Error: complete todos los campos.", fg="red")

# Función para limpiar los campos de entrada
def limpiar_campos():
    #entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    combobox_tipo.set('')  # Limpiar el Combobox
    entry_direccion.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)

# Función para cerrar la ventana
def salir():
    ventana.destroy()

def iniciar_ventana():
    global entry_id, entry_nombre, entry_apellido, combobox_tipo, entry_direccion, entry_telefono, ventana, lbl_validacion

    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Formulario de Registro de Usuario")
    ventana.geometry("600x900")
    ventana.configure(bg="#F0F4F8")  # Fondo suave

    # Estilos
    fuente_titulo = font.Font(family="Helvetica", size=16, weight="bold")
    fuente_label = font.Font(family="Arial", size=11)
    fuente_entry = font.Font(family="Arial", size=10)

    # Frame para el contenido
    frame = tk.Frame(ventana, padx=20, pady=20, bg="#FFFFFF", relief="solid", bd=2)
    frame.pack(pady=20, padx=10, fill="both", expand=True)

    # Título
    label_titulo = tk.Label(frame, text="Registrar Usuario", font=fuente_titulo, bg="#FFFFFF", fg="#333333")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # ID
    #tk.Label(frame, text="ID:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=1, column=0, sticky="e", padx=10, pady=8)
    #entry_id = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    #entry_id.grid(row=1, column=1, pady=8)

    # Nombre
    tk.Label(frame, text="Nombre:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=1, column=0, sticky="e", padx=10, pady=8)
    entry_nombre = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_nombre.grid(row=1, column=1, pady=8)

    # Apellido
    tk.Label(frame, text="Apellido:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=2, column=0, sticky="e", padx=10, pady=8)
    entry_apellido = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_apellido.grid(row=2, column=1, pady=8)

    # Tipo
    tk.Label(frame, text="Tipo:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=3, column=0, sticky="e", padx=10, pady=8)

    # Lista de tipos de usuarios ("Estudiante" y "Profesor")
    tipos = ['Estudiante', 'Profesor']  # Opciones limitadas a Estudiante y Profesor

    combobox_tipo = ttk.Combobox(frame, values=tipos, font=fuente_entry, width=23, state="readonly")
    combobox_tipo.grid(row=3, column=1, pady=8)
    combobox_tipo.set('')  # Limpiar el Combobox al inicio

    # Dirección
    tk.Label(frame, text="Dirección:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=4, column=0, sticky="e", padx=10, pady=8)
    entry_direccion = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_direccion.grid(row=4, column=1, pady=8)

    # Teléfono
    tk.Label(frame, text="Teléfono:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=5, column=0, sticky="e", padx=10, pady=8)
    entry_telefono = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_telefono.grid(row=5, column=1, pady=8)

    # Botón enviar
    boton_enviar = tk.Button(frame, text="Enviar", command=enviar_datos,
                             bg="#4CAF50", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_enviar.grid(row=6, column=0, columnspan=2, pady=10)

    # Botón salir
    boton_salir = tk.Button(frame, text="Salir", command=salir, bg="#f44336", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_salir.grid(row=7, column=0, columnspan=2, pady=10)

    # Etiqueta de validación
    lbl_validacion = tk.Label(frame, text="", font=fuente_label, bg="#FFFFFF", fg="red")
    lbl_validacion.grid(row=8, column=0, columnspan=2, pady=10)

    ventana.mainloop()
