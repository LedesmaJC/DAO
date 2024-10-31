import sqlite3

from datos.DBConnection import DBConnection

# Instanciamos el singleton
db = DBConnection('datos/TPI_DAO.db')

# Obtenemos la conexión
connection = db.get_connection()

# Guardar los datos del libro en la base de datos
def consultar_libros_disponibles():
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT libro FROM libros WHERE libro.disponible = 'SI'
                """ 
            )
        except sqlite3.IntegrityError as e:
            raise Exception("Error durante la búsqueda: " + str(e))  # Lanza la excepción para manejar en la GUI
        except sqlite3.Error as e:
            raise Exception("Error durante la búsqueda: " + str(e))  # Lanza la excepción para manejar en la GUI
        finally:
            if cursor:  # Solo cerramos el cursor si fue creado
                cursor.close()
    else:
        raise Exception("No se pudo realizar la operación por problemas de conexión.")
