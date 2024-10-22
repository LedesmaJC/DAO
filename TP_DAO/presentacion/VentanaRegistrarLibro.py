import tkinter as tk
from tkinter import font
from tkinter import ttk  # Importa ttk para usar Combobox
from entidades.Libro import Libro
from controladores import ControladorLibro as c_l  # Controlador para manejar la lógica de guardar el libro
from controladores import ControladorAutor as c_a  # Controlador para obtener los autores

def enviar_datos():
    isbn = entry_isbn.get()
    titulo = entry_titulo.get()
    genero = entry_genero.get()
    anioPublicacion = entry_anioPublicacion.get()
    stock = entry_stock.get()

    if isbn and titulo and genero and anioPublicacion and stock:
        autor_id = combobox_autor.get()  # Obtiene el ID del autor seleccionado
        disponible =  combobox_disponible.get()
        libro = Libro(isbn, titulo, genero, anioPublicacion, autor_id, stock, disponible)

        try:
            c_l.guardar_libro(libro)
            limpiar_campos()  # Limpiar los campos después de enviar
            lbl_validacion.config(text="", fg="#333333")  # Limpiar mensaje de error
            lbl_validacion.config(text="Libro registrado correctamente.", fg="Green")    
            print("Datos del libro enviados correctamente.")
        except Exception as e:
            lbl_validacion.config(text=f"Error: {str(e)}", fg="red")  # Actualizar mensaje de error
    else:
        lbl_validacion.config(text="Error: complete todos los campos.", fg="red")

# Función para limpiar los campos de entrada
def limpiar_campos():
    entry_isbn.delete(0, tk.END)
    entry_titulo.delete(0, tk.END)
    entry_genero.delete(0, tk.END)
    entry_anioPublicacion.delete(0, tk.END)
    combobox_autor.set('')  # Limpiar el Combobox
    entry_stock.delete(0, tk.END)
    combobox_disponible.delete(0, tk.END)

# Función para cerrar la ventana
def salir():
    ventana.destroy()

def iniciar_ventana():
    global entry_isbn, entry_titulo, entry_genero, entry_anioPublicacion, entry_stock, combobox_autor, ventana, lbl_validacion,  combobox_disponible

    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Formulario de Registro de Libro")
    ventana.geometry("600x900")
    ventana.configure(bg="#F0F4F8")  # Fondo más suave

    # Estilos
    fuente_titulo = font.Font(family="Helvetica", size=16, weight="bold")
    fuente_label = font.Font(family="Arial", size=11)
    fuente_entry = font.Font(family="Arial", size=10)

    # Frame para el contenido
    frame = tk.Frame(ventana, padx=20, pady=20, bg="#FFFFFF", relief="solid", bd=2)
    frame.pack(pady=20, padx=10, fill="both", expand=True)

    # Título
    label_titulo = tk.Label(frame, text="Registrar Libro", font=fuente_titulo, bg="#FFFFFF", fg="#333333")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # ISBN
    tk.Label(frame, text="ISBN:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=1, column=0, sticky="e", padx=10, pady=8)
    entry_isbn = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_isbn.grid(row=1, column=1, pady=8)

    # Título
    tk.Label(frame, text="Título:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=2, column=0, sticky="e", padx=10, pady=8)
    entry_titulo = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_titulo.grid(row=2, column=1, pady=8)

    # Género
    tk.Label(frame, text="Género:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=3, column=0, sticky="e", padx=10, pady=8)
    entry_genero = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_genero.grid(row=3, column=1, pady=8)

    # Año de Publicación
    tk.Label(frame, text="Año de Publicación:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=4, column=0, sticky="e", padx=10, pady=8)
    entry_anioPublicacion = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_anioPublicacion.grid(row=4, column=1, pady=8)

    # Autor
    tk.Label(frame, text="Autor:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=5, column=0, sticky="e", padx=10, pady=8)

    autores = c_a.obtener_autores()  # Suponiendo que retorna una lista de tuplas (id, nombre, apellido)
    autores_nombres = [(id, f"{nombre} {apellido}") for id, nombre, apellido in autores]  # Formato "Nombre Apellido"

    combobox_autor = ttk.Combobox(frame, values=autores_nombres, font=fuente_entry, width=23, state="readonly")
    combobox_autor.grid(row=5, column=1, pady=8)

    # Cambiar la forma de establecer el valor seleccionado
    combobox_autor.set('')  # Limpiar el Combobox al inicio

    # Stock
    tk.Label(frame, text="Stock:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=6, column=0, sticky="e", padx=10, pady=8)
    entry_stock = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_stock.grid(row=6, column=1, pady=8)
    
    # Disponible
    tk.Label(frame, text="Disponible:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=7, column=0, sticky="e", padx=10, pady=8)

    # Lista de tipos de usuarios ("SI" y "NO")
    dispo = ['SI', 'NO']  

    combobox_disponible = ttk.Combobox(frame, values=dispo, font=fuente_entry, width=23, state="readonly")
    combobox_disponible.grid(row=7, column=1, pady=8)
    combobox_disponible.set('')  # Limpiar el Combobox al inicio

    # Botón enviar
    boton_enviar = tk.Button(frame, text="Enviar", command=enviar_datos,
                             bg="#4CAF50", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_enviar.grid(row=8, column=0, columnspan=2, pady=10)

    # Botón salir
    boton_salir = tk.Button(frame, text="Salir", command=salir, bg="#f44336", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_salir.grid(row=9, column=0, columnspan=2, pady=10)
     
     # Etiquetas de validacion
    lbl_validacion = tk.Label(frame, text="", font=fuente_label, bg="#FFFFFF", fg="red")
    lbl_validacion.grid(row=10, column=0, columnspan=2, pady=10)

    ventana.mainloop()
