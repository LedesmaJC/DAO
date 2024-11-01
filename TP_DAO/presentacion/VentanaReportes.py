import tkinter as tk
from tkinter import font
from tkinter import ttk  # Importa ttk para usar Combobox

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
    boton_enviar = tk.Button(frame, text="Seleccionar", command="Cambiar",
                             bg="#4CAF50", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_enviar.grid(row=3, column=0, columnspan=2, pady=10)

    # Botón salir
    boton_salir = tk.Button(frame, text="Salir", command=salir, bg="#f44336", fg="white", padx=15, pady=5, font=fuente_label, relief="raised", bd=3)
    boton_salir.grid(row=3, column=2, columnspan=2, pady=10)
     
     # Etiquetas de validacion
    lbl_validacion = tk.Label(frame, text="", font=fuente_label, bg="#FFFFFF", fg="red")
    lbl_validacion.grid(row=5, column=0, columnspan=2, pady=10)

    ventana.mainloop()
