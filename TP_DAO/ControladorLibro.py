import sqlite3

# Conectar a la base de datos
def conectar_base_datos():
    try:
        connection = sqlite3.connect('TPI_DAO.db')
        return connection
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Guardar los datos del libro en la base de datos
def guardar_libro(libro):
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute(
                """
                INSERT INTO libros (isbn, titulo, genero, anio_publicacion, autor, stock)
                VALUES (?, ?, ?, ? , ?, ?)
                """, 
                (libro.isbn, libro.titulo, libro.genero, libro.anioPublicacion, libro.autor, libro.stock)
            )
            conexion.commit()
            print("Libro guardado correctamente.")
        except sqlite3.IntegrityError as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        except sqlite3.Error as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        finally:
            cursor.close()
            conexion.close()
    else:
        raise Exception("No se pudo realizar la operación por problemas de conexión.")
