import sqlite3

# Conectar a la base de datos
def conectar_base_datos():
    try:
        connection = sqlite3.connect('datos/TPI_DAO.db')
        return connection
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
    
# Guardar los datos del prestamo en la base de datos
def prestar(prestamo):
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute(
                """
                INSERT INTO prestamos (usuario, libro, f_prestamo, f_devolucion_estimada)
                VALUES (?, ?, ? , ?)
                """, 
                (prestamo.usuario, prestamo.libro, prestamo.f_prestamo, prestamo.f_devolucion_estimada)
            )
            conexion.commit()
            print("Prestamo registrado correctamente.")
        except sqlite3.IntegrityError as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        except sqlite3.Error as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        finally:
            cursor.close()
            conexion.close()
    else:
        raise Exception("No se pudo realizar la operación por problemas de conexión.")
