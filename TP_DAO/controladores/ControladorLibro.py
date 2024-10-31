import sqlite3

from datos.DBConnection import DBConnection

# Instanciamos el singleton
db = DBConnection('datos/TPI_DAO.db')

# Obtenemos la conexión
connection = db.get_connection()
    
def consultar_libros_disponibles():
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                SELECT * FROM libros WHERE stock > 0
                """ 
            )
            libros_disponibles = cursor.fetchall()  # Obtener todos los resultados
            return libros_disponibles
        except sqlite3.IntegrityError as e:
            raise Exception("Error durante la búsqueda: " + str(e))  # Lanza la excepción para manejar en la GUI
        except sqlite3.Error as e:
            raise Exception("Error durante la búsqueda: " + str(e))  # Lanza la excepción para manejar en la GUI
        finally:
            if cursor:  # Solo cerramos el cursor si fue creado
                cursor.close()
    else:
        raise Exception("No se pudo realizar la operación por problemas de conexión.")
    
    


# Guardar los datos del libro en la base de datos
def guardar_libro(libro):
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO libros (isbn, titulo, genero, anio_publicacion, autor, stock)
                VALUES (?, ?, ?, ? , ?, ?)
                """, 
                (libro.isbn, libro.titulo, libro.genero, libro.anioPublicacion, libro.autor, libro.stock)
            )
            connection.commit()
            print("Libro guardado correctamente.")
        except sqlite3.IntegrityError as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        except sqlite3.Error as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        finally:
            if cursor:  # Solo cerramos el cursor si fue creado
                cursor.close()
    else:
        raise Exception("No se pudo realizar la operación por problemas de conexión.")
