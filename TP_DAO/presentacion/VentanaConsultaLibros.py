import tkinter as tk
from tkinter import font
from tkinter import ttk  # Importa ttk para usar Combobox
from entidades.Libro import Libro
from controladores import ControladorLibro as c_l  # Controlador para manejar la lógica de guardar el libro
from controladores import ControladorAutor as c_a  # Controlador para obtener los autores


# Función para cerrar la ventana
def salir():
    ventana.destroy()


def iniciar_ventana():
    global ventana, lbl_validacion, root, fuente_label, frame

    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Formulario de Registro de Libro")
    ventana.geometry("900x900")  # Tamaño ajustado para una mejor visualización
    ventana.configure(bg="#F0F4F8")  # Fondo más suave
    
    # Fuente para encabezados
    fuente_encabezado = font.Font(family="Helvetica", size=10, weight="bold")
    
    # Crear el Treeview
    columns = ('#1', '#2', '#3', '#4', '#5', '#6')
    tree = ttk.Treeview(ventana, columns=columns, show='headings', height=15)

    # Configurar los encabezados de las columnas con estilos
    tree.heading('#1', text='ISBN', anchor='center')
    tree.heading('#2', text='Título', anchor='center')
    tree.heading('#3', text='Género', anchor='center')
    tree.heading('#4', text='Publicación', anchor='center')
    tree.heading('#5', text='Autor', anchor='center')
    tree.heading('#6', text='Stock', anchor='center')

    # Estilo de columnas
    tree.column('#1', width=100, anchor='center')
    tree.column('#2', width=200, anchor='w')  # Alinear el título a la izquierda
    tree.column('#3', width=100, anchor='center')
    tree.column('#4', width=100, anchor='center')
    tree.column('#5', width=150, anchor='center')
    tree.column('#6', width=100, anchor='center')

    style = ttk.Style()
    style.configure("Treeview", rowheight=25, font=('Helvetica', 10))
    style.configure("Treeview.Heading", font=fuente_encabezado, background="#4CAF50", foreground="white")  # Estilo de encabezados
    style.map('Treeview', background=[('selected', '#4285F4')], foreground=[('selected', 'white')])
    style.configure("Treeview", background="#f9f9f9", fieldbackground="#f9f9f9")
    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Evita el borde interior

    libros = c_l.consultar_libros_disponibles()

    # Insertar datos en la tabla
    for index, row in enumerate(libros):
        tag = 'even' if index % 2 == 0 else 'odd'
        tree.insert('', tk.END, values=row, tags=(tag,))

    tree.tag_configure('even', background='#EAF2F8')
    tree.tag_configure('odd', background='#D5DBDB')

    tree.pack(expand=True, fill='both', padx=20, pady=20)

    # Crear frame para botones
    frame_botones = tk.Frame(ventana, bg="#F0F4F8")
    frame_botones.pack(pady=10)

    # Botón salir
    boton_salir = tk.Button(frame_botones, text="Salir", command=salir, bg="#f44336", fg="white", padx=20, pady=10, font=font.Font(size=10, weight="bold"), relief="raised", bd=3)
    boton_salir.grid(row=0, column=0, padx=10)

    # Etiquetas de validación
    lbl_validacion = tk.Label(frame_botones, text="", font=font.Font(size=10), bg="#F0F4F8", fg="red")
    lbl_validacion.grid(row=1, column=0, pady=10)

    ventana.mainloop()

