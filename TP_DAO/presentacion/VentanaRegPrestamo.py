import tkinter as tk
import tkcalendar as tkc
from tkinter import font
from tkinter import ttk
from tkcalendar import DateEntry 
from datetime import date
from entidades.Prestamo import Prestamo
from controladores import ControladorPrestamo as c_p  # Controlador para manejar la lógica de guardar el préstamo
from controladores import ControladorUsuario as c_u  # Controlador para obtener los usuarios
from controladores import ControladorLibro as c_l  # Controlador para obtener los libros

def enviar_prestamo():
    usuario_id = combobox_usuarios.get()
    libro_id = combobox_libros.get()
    # Obtener la fecha actual
    fecha_actual = date.today()
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
    f_prestamo = fecha_formateada
    f_devolucion_estimada = entry_f_devolucion_estimada.get_date()

    if f_devolucion_estimada < fecha_actual:
        lbl_validacion.config(text="Error: La fecha de devolución no puede ser anterior a la de préstamo.", fg="red")
        return

    if usuario_id and libro_id and f_prestamo and f_devolucion_estimada:
        prestamo = Prestamo(usuario_id, libro_id, f_prestamo, f_devolucion_estimada)

        try:
            c_p.prestar(prestamo)
            limpiar_campos()
            lbl_validacion.config(text="Préstamo registrado correctamente.", fg="green")
        except Exception as e:
            lbl_validacion.config(text=f"Error: {str(e)}", fg="red")
    else:
        lbl_validacion.config(text="Error: complete todos los campos obligatorios.", fg="red")

def limpiar_campos():
    combobox_usuarios.set('')
    combobox_libros.set('')
    entry_f_devolucion_estimada.delete(0, tk.END)

def salir():
    ventana.destroy()

def iniciar_ventana_prestamo():
    global combobox_usuarios, combobox_libros, entry_f_devolucion_estimada, lbl_validacion, ventana

    ventana = tk.Tk()
    ventana.title("Formulario de Registro de Préstamo")
    ventana.geometry("600x800")
    ventana.configure(bg="#F0F4F8")

    fuente_titulo = font.Font(family="Helvetica", size=16, weight="bold")
    fuente_label = font.Font(family="Arial", size=11)
    fuente_entry = font.Font(family="Arial", size=10)

    frame = tk.Frame(ventana, padx=20, pady=20, bg="#FFFFFF", relief="solid", bd=2)
    frame.pack(pady=20, padx=10, fill="both", expand=True)

    label_titulo = tk.Label(frame, text="Registrar Préstamo", font=fuente_titulo, bg="#FFFFFF", fg="#333333")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # Usuario
    tk.Label(frame, text="Usuario:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=1, column=0, sticky="e", padx=10, pady=8)
    
    usuarios = c_u.obtener_usuarios()  # Devuelve una lista de tuplas con los datos de los usuarios
    nombres_usuarios = [f"{usuario[1]} {usuario[2]}" for usuario in usuarios]  
    
    combobox_usuarios = ttk.Combobox(frame, values=nombres_usuarios, font=fuente_entry, width=23, state="readonly")
    combobox_usuarios.grid(row=1, column=1, pady=8)

    # Libro
    tk.Label(frame, text="Libro:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=2, column=0, sticky="e", padx=10, pady=8)
    
    # Obtener libros disponibles y agregar al Combobox
    libros_disponibles = c_l.consultar_libros_disponibles()  # Devuelve una lista de tuplas con los datos de los libros
    titulos_libros = [libro[1] for libro in libros_disponibles]  
    
    combobox_libros = ttk.Combobox(frame, values=titulos_libros, font=fuente_entry, width=23, state="readonly")
    combobox_libros.grid(row=2, column=1, pady=8)


    # Fecha de devolución estimada (DateEntry)
    tk.Label(frame, text="Fecha Devolución Estimada:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=3, column=0, sticky="e", padx=10, pady=8)
    entry_f_devolucion_estimada = DateEntry(frame, font=fuente_entry, width=23, background="darkblue", foreground="white", borderwidth=2)
    entry_f_devolucion_estimada.grid(row=3, column=1, pady=8)

    # Botón enviar
    boton_enviar = tk.Button(frame, text="Enviar", command=enviar_prestamo, bg="#4CAF50", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_enviar.grid(row=4, column=0, columnspan=2, pady=10)

    # Botón salir
    boton_salir = tk.Button(frame, text="Salir", command=salir, bg="#f44336", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_salir.grid(row=5, column=0, columnspan=2, pady=10)

    # Etiqueta de validación
    lbl_validacion = tk.Label(frame, text="", font=fuente_label, bg="#FFFFFF", fg="red")
    lbl_validacion.grid(row=7, column=0, columnspan=2, pady=10)

    ventana.mainloop()

