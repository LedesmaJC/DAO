import tkinter as tk
from tkinter import font
from tkinter import ttk
from entidades.Prestamo import Prestamo
from datetime import date
from controladores import ControladorPrestamo as c_p  # Controlador para manejar la lógica de guardar el préstamo
from controladores import ControladorUsuario as c_u  # Controlador para obtener los usuarios

def enviar_devolucion():
    prestamo_seleccionado = combobox_prestamos.get()

    # Obtener la fecha actual
    fecha_actual = date.today()
    fecha_formateada = fecha_actual.strftime("%d/%m/%Y")
    f_devolucion_real = fecha_formateada
    observacion = entry_observacion.get()
    
    # Validar que los campos no estén vacíos
    if not prestamo_seleccionado or not observacion:
        lbl_validacion.config(text="Error: complete todos los campos obligatorios.", fg="red")
        return  # Salir de la función si falta información

    try:
        id_prestamo = int(prestamo_seleccionado.split()[0])  # Suponiendo que el ID está al principio
        print(f"ID del préstamo seleccionado: {id_prestamo}")  # Mensaje de depuración

        # Aquí podrías consultar si el préstamo tiene un libro asociado
        prestamo = c_p.buscar_id(id_prestamo)  
        if prestamo is None or prestamo.libro is None:
            raise Exception("No se encontró el libro asociado al préstamo.")

        c_p.devolver(id_prestamo, f_devolucion_real, observacion)
        limpiar_campos()
        lbl_validacion.config(text="Devolución registrada correctamente.", fg="green")
    except Exception as e:
        lbl_validacion.config(text=f"Error: {str(e)}", fg="red")

def limpiar_campos():
    combobox_prestamos.set('')
    entry_observacion.delete(0, tk.END)
    
def salir():
    ventana.destroy()

def iniciar_ventana_devolucion():
    global combobox_prestamos, entry_observacion, lbl_validacion, ventana

    ventana = tk.Tk()
    ventana.title("Formulario de Registro de Devolución")
    ventana.geometry("600x800")
    ventana.configure(bg="#F0F4F8")

    fuente_titulo = font.Font(family="Helvetica", size=16, weight="bold")
    fuente_label = font.Font(family="Arial", size=11)
    fuente_entry = font.Font(family="Arial", size=10)

    frame = tk.Frame(ventana, padx=20, pady=20, bg="#FFFFFF", relief="solid", bd=2)
    frame.pack(pady=20, padx=10, fill="both", expand=True)

    label_titulo = tk.Label(frame, text="Registrar Devolución", font=fuente_titulo, bg="#FFFFFF", fg="#333333")
    label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 15))

    # Prestamo
    tk.Label(frame, text="Préstamos:", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=1, column=0, sticky="e", padx=10, pady=8)
    
    prestamos = c_p.buscar() 
    id_prestamos = [f"{prestamo.id} {prestamo.usuario} {prestamo.libro}" for prestamo in prestamos]
    combobox_prestamos = ttk.Combobox(frame, values=id_prestamos, font=fuente_entry, width=23, state="readonly")
    combobox_prestamos.grid(row=1, column=1, pady=8)

        # Observación
    tk.Label(frame, text="Observación", font=fuente_label, bg="#FFFFFF", fg="#666666").grid(row=2, column=0, sticky="e", padx=10, pady=8)
    entry_observacion = tk.Entry(frame, font=fuente_entry, width=25, bd=2, relief="groove")
    entry_observacion.grid(row=2, column=1, pady=8)

    # Botón enviar
    boton_enviar = tk.Button(frame, text="Enviar", command=lambda: enviar_devolucion(), bg="#4CAF50", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_enviar.grid(row=3, column=0, columnspan=2, pady=10)


    # Botón salir
    boton_salir = tk.Button(frame, text="Salir", command=salir, bg="#f44336", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_salir.grid(row=4, column=0, columnspan=2, pady=10)

    # Etiqueta de validación
    lbl_validacion = tk.Label(frame, text="", font=fuente_label, bg="#FFFFFF", fg="red")
    lbl_validacion.grid(row=5, column=0, columnspan=2, pady=10)

    ventana.mainloop()

