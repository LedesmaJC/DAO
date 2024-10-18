import sqlite3
import VentanaRegAutor as vent

# Iniciar la ventana y capturar los datos
vent.iniciar_ventana()
datos_form = vent.enviar_datos()

# Conectar a la base de datos
connection = sqlite3.connect('TPI_DAO.db')
cursor = connection.cursor()

# Insertar datos
try:
    cursor.execute("INSERT INTO autores (nombre, apellido, nacionalidad) VALUES (?, ?, ?)",
                   (datos_form.nombre, datos_form.apellido, datos_form.nacionalidad))
    connection.commit()
    print("Transacción completada")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    cursor.close()
    connection.close()
