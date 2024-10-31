import sqlite3
from datos.DBConnection import DBConnection

# Instanciamos el singleton
db = DBConnection('datos/TPI_DAO.db')

# Obtenemos la conexión
connection = db.get_connection()

# Guardar los datos del prestamo en la base de datos
def prestar(prestamo):
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()

            # Insertar préstamo en la tabla prestamos
            cursor.execute(
                """
                INSERT INTO prestamos (usuario, libro, f_prestamo, f_devolucion_estimada)
                VALUES (?, ?, ?, ?)
                """, 
                (prestamo.usuario, prestamo.libro, prestamo.f_prestamo, prestamo.f_devolucion_estimada)
            )

            # Verificar si el libro existe antes de actualizar
            cursor.execute(
                "SELECT stock FROM libros WHERE titulo = ?",
                (prestamo.libro,)
            )
            stock_actual = cursor.fetchone()
            
                # Actualizar el stock del libro restando 1
            cursor.execute(
                    """
                    UPDATE libros
                    SET stock = stock - 1
                    WHERE titulo = ?
                    """,
                    (prestamo.libro,)
                )

            connection.commit()
            print("Préstamo registrado y stock actualizado correctamente.")
        except sqlite3.IntegrityError as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        except sqlite3.Error as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        finally:
            if cursor:  # Solo cerramos el cursor si fue creado
                cursor.close()
    else:
        raise Exception("No se pudo realizar la operación por problemas de conexión.")

# Registrar la devolución y actualizar el stock
def devolver(prestamo, f_dev, obs):
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()

            # Primero obtenemos el libro asociado al préstamo
            cursor.execute(
                """
                SELECT libro FROM prestamos WHERE id = ?
                """,
                (prestamo,)  # Aquí usamos el ID del préstamo
            )
            libro_id = cursor.fetchone()  # Obtenemos el ID del libro

            if libro_id:
                # Verificar stock actual antes de actualizar
                cursor.execute(
                    "SELECT stock FROM libros WHERE titulo = ?",
                    (libro_id[0],)
                )
                stock_actual = cursor.fetchone()
                    # Actualizar la devolución en la tabla de préstamos
                cursor.execute(
                        """
                        UPDATE prestamos
                        SET f_devolucion_real = ?, observacion = ?
                        WHERE id = ?
                        """, 
                        (f_dev, obs, prestamo)
                    )

                    # Actualizar el stock del libro sumándole 1
                cursor.execute(
                        """
                        UPDATE libros
                        SET stock = stock + 1
                        WHERE titulo = ?
                        """,
                        (libro_id[0],)
                    )
                connection.commit()
                print("Devolución registrada y stock actualizado correctamente.")
            else:
                raise Exception("No se encontró el libro asociado al préstamo.")
        except sqlite3.IntegrityError as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        except sqlite3.Error as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        finally:
            if cursor:  # Solo cerramos el cursor si fue creado
                cursor.close()
    else:
        raise Exception("No se pudo realizar la operación por problemas de conexión.")

def buscar():
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM prestamos WHERE f_devolucion_real is NULL")
            prestamos = cursor.fetchall()
            
            if prestamos:
                # Crear una lista de diccionarios para cada préstamo
                lista_prestamos = []
                for prestamo in prestamos:
                    lista_prestamos.append({
                        'id': prestamo[0],
                        'usuario': prestamo[1],
                        'libro': prestamo[2],
                        'f_prestamo': prestamo[3],
                        'f_devolucion_estimada': prestamo[4]
                    })
                return lista_prestamos
            else:
                print("No se encontraron préstamos.")
                return []
        except sqlite3.Error as e:
            raise Exception("Error durante la búsqueda: " + str(e))  # Lanza la excepción para manejar en la GUI
        finally:
            if cursor:  # Solo cerramos el cursor si fue creado
                cursor.close()
    else:
        raise Exception("No se pudo realizar la operación por problemas de conexión.")
