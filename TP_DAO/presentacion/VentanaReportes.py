from datetime import date
import tkinter as tk
from tkinter import font
from tkinter import ttk  # Importa ttk para usar Combobox
import controladores.ControladorReportes as c_r
import controladores.ControladorPrestamo as c_p


def iniciar_reporte():
    opcion = combobox_reporte.get()
    if opcion == "Reporte 1":
        iniciar_ventana_rep_uno()
import tkinter as tk
from tkinter import ttk, font
from datetime import date

import tkinter as tk
from tkinter import ttk, font
from datetime import date

import tkinter as tk
from tkinter import ttk, font
from datetime import date

def iniciar_ventana_rep_uno():
    global lbl_validacion_uno
    # Crear la ventana
    ventana_uno = tk.Tk()
    ventana_uno.title("Reporte de Préstamos")
    ventana_uno.geometry("900x900")  # Tamaño ajustado para una mejor visualización
    ventana_uno.configure(bg="#F0F4F8")  # Fondo más suave
    
    # Fuente para encabezados
    fuente_encabezado = font.Font(family="Helvetica", size=10, weight="bold")
    
    # Obtener la lista de préstamos vencidos
    prestamos_vencidos = c_r.reporte_uno()
    cantidad_vencidos = len(prestamos_vencidos)

    # Etiqueta para mostrar la cantidad de préstamos vencidos
    lbl_cantidad_vencidos = tk.Label(ventana_uno, text=f"La cantidad de préstamos vencidos es: {cantidad_vencidos}", font=font.Font(size=12), bg="#F0F4F8", fg="black")
    lbl_cantidad_vencidos.pack(pady=10)

    # Crear el Treeview
    columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7')
    tree = ttk.Treeview(ventana_uno, columns=columns, show='headings', height=15)

    # Configurar los encabezados de las columnas con estilos
    tree.heading('#1', text='ID', anchor='center')
    tree.heading('#2', text='Usuario', anchor='center')
    tree.heading('#3', text='Libro', anchor='center')
    tree.heading('#4', text='Fecha Préstamo', anchor='center')
    tree.heading('#5', text='Fecha Devolución Estimada', anchor='center')
    tree.heading('#6', text='Fecha Devolución Real', anchor='center')
    tree.heading('#7', text='Observación', anchor='center')

    # Estilo de columnas
    tree.column('#1', width=100, anchor='center')
    tree.column('#2', width=200, anchor='w')  # Alinear el título a la izquierda
    tree.column('#3', width=100, anchor='center')
    tree.column('#4', width=100, anchor='center')
    tree.column('#5', width=150, anchor='center')
    tree.column('#6', width=100, anchor='center')
    tree.column('#7', width=100, anchor='center')

    # Estilo general de la tabla
    style = ttk.Style()
    style.configure("Treeview", rowheight=25, font=('Helvetica', 10))
    style.configure("Treeview.Heading", font=fuente_encabezado, background="#4CAF50", foreground="white")
    style.map('Treeview', background=[('selected', '#4285F4')], foreground=[('selected', 'white')])
    style.configure("Treeview", background="#f9f9f9", fieldbackground="#f9f9f9")
    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Evita el borde interior

    # Obtener la lista de objetos Prestamo
    prestamos = c_r.reporte_uno()
    if prestamos is None:
        #lbl_validacion_uno.config(text="Error: La búsqueda de préstamos devolvió None.", fg="red")
        prestamos = []  # Si es None, asigna una lista vacía

    # Insertar datos en la tabla
    for index, prestamo in enumerate(prestamos):
        # Determinar el tag basado en la paridad del índice
        tag = 'even' if index % 2 == 0 else 'odd'
        
        # Asignar valores a variables para mejorar la legibilidad
        id_prestamo = prestamo.id
        usuario = prestamo.usuario
        libro = prestamo.libro
        fecha_prestamo = prestamo.f_prestamo
        f_devolucion_estimada = prestamo.f_devolucion_estimada
        f_devolucion_real = prestamo.f_devolucion_real or 'Pendiente'  # Valor predeterminado si es None
        observacion = prestamo.observacion or 'Ninguna'  # Valor predeterminado si es None

        # Insertar el préstamo en la fila correspondiente
        tree.insert('', tk.END, values=(
            id_prestamo,
            usuario,
            libro,
            fecha_prestamo,
            f_devolucion_estimada,
            f_devolucion_real,
            observacion
        ), tags=(tag,))

    # Configurar colores alternados en las filas
    tree.tag_configure('even', background='#EAF2F8')
    tree.tag_configure('odd', background='#D5DBDB')

    # Mostrar la tabla
    tree.pack(expand=True, fill='both', padx=20, pady=20)

    # Crear frame para botones
    frame_botones = tk.Frame(ventana_uno, bg="#F0F4F8")
    frame_botones.pack(pady=10)

    # Botón salir
    boton_salir = tk.Button(frame_botones, text="Salir", command=ventana_uno.destroy, bg="#f44336", fg="white", padx=20, pady=10, font=font.Font(size=10, weight="bold"), relief="raised", bd=3)
    boton_salir.grid(row=0, column=0, padx=10)

    # Etiqueta de validación para mostrar mensajes adicionales
    lbl_validacion_uno = tk.Label(frame_botones, text="", font=font.Font(size=10), bg="#F0F4F8", fg="red")
    lbl_validacion_uno.grid(row=1, column=0, pady=10)

    ventana_uno.mainloop()



def salir():
    ventana.destroy()

def iniciar_ventana():
    global combobox_reporte, ventana, lbl_validacion

    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Selección de reporte")
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
    label_titulo = tk.Label(frame, text="Selección de Reporte", font=fuente_titulo, bg="#FFFFFF", fg="#333333")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))


    # Reporte
    tk.Label(frame, text="Reporte:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=1, column=0, sticky="e", padx=10, pady=8)

    reportes_nombres = ["Reporte 1", "Reporte 2", "Reporte 3"]  

    combobox_reporte = ttk.Combobox(frame, values=reportes_nombres, font=fuente_entry, width=23, state="readonly")
    combobox_reporte.grid(row=1, column=1, pady=8)

    # Cambiar la forma de establecer el valor seleccionado
    combobox_reporte.set('')  # Limpiar el Combobox al inicio
    
    # Botón Seleccionar
    boton_enviar = tk.Button(frame, text="Seleccionar", command=iniciar_reporte,
                             bg="#4CAF50", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_enviar.grid(row=3, column=0, columnspan=2, pady=10)

    # Botón salir
    boton_salir = tk.Button(frame, text="Salir", command=salir, bg="#f44336", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_salir.grid(row=3, column=2, columnspan=2, pady=10)
     
     # Etiquetas de validacion
    lbl_validacion = tk.Label(frame, text="", font=fuente_label, bg="#FFFFFF", fg="red")
    lbl_validacion.grid(row=5, column=0, columnspan=2, pady=10)

    ventana.mainloop()
