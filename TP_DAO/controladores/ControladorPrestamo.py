import sqlite3
from entidades.Prestamo import Prestamo
from datos.DBConnection import DBConnection
from datetime import date, datetime


# Instanciamos el singleton
db = DBConnection('datos/TPI_DAO.db')

# Obtenemos la conexión
connection = db.get_connection()

def prestar(prestamo: Prestamo):
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
            
            if stock_actual and stock_actual[0] > 0:  # Verifica si hay stock disponible
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
            else:
                raise Exception("No hay stock disponible para el libro.")

        except sqlite3.IntegrityError as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        except sqlite3.Error as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        finally:
            if cursor:  # Solo cerramos el cursor si fue creado
                cursor.close()
    else:
        raise Exception("No se pudo realizar la operación por problemas de conexión.")


def devolver(prestamo_id, f_dev: str, obs: str):
    with db.get_connection() as connection:
        cursor = connection.cursor()
        try:
            # Primero obtenemos el libro asociado al préstamo
            cursor.execute(
                """
                SELECT libro FROM prestamos WHERE id = ?
                """,
                (prestamo_id,)
            )
            libro_id = cursor.fetchone()

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
                    (f_dev, obs, prestamo_id)
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
            raise Exception("Error durante la inserción: " + str(e))
        except sqlite3.Error as e:
            raise Exception("Error durante la inserción: " + str(e))

#Busca los que no estan devueltos en realidad
def buscar_id(id):
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM prestamos WHERE id = ?",(id,))
            prestamo = cursor.fetchone()

            if prestamo:
                    p = Prestamo(
                        usuario=prestamo[1],
                        libro=prestamo[2],
                        f_prestamo=prestamo[3],
                        f_devolucion_estimada=prestamo[4],
                    )
                    p.id = prestamo[0]
                    p.f_devolucion_real = prestamo[5]
                    p.observacion = prestamo[6]

                    return p
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

#Busca los que no estan devueltos en realidad
def buscar():
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM prestamos WHERE f_devolucion_real is NULL")
            prestamos = cursor.fetchall()

            if prestamos:
                lista_prestamos = []
                for prestamo in prestamos:
                    # Crear un objeto Prestamo por cada fila de la base de datos
                    p = Prestamo(
                        usuario=prestamo[1],
                        libro=prestamo[2],
                        f_prestamo=prestamo[3],
                        f_devolucion_estimada=prestamo[4],
                    )
                    p.id = prestamo[0]
                    p.f_devolucion_real = prestamo[5]
                    p.observacion = prestamo[6]

                    lista_prestamos.append(p)
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

def buscar_todos():
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM prestamos")
            prestamos = cursor.fetchall()

            if prestamos:
                lista_prestamos = []
                for prestamo in prestamos:
                    # Crear un objeto Prestamo por cada fila de la base de datos
                    p = Prestamo(
                        usuario=prestamo[1],
                        libro=prestamo[2],
                        f_prestamo=prestamo[3],
                        f_devolucion_estimada=prestamo[4],
                    )
                    p.id = prestamo[0]
                    p.f_devolucion_real = prestamo[5]
                    p.observacion = prestamo[6]

                    lista_prestamos.append(p)
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

    
def buscar_vencidos():
    # Obtener la fecha actual
    fecha_actual = date.today()

    # Consultar todos los préstamos
    prestamos = buscar()

    # Formato esperado de la fecha en las columnas de la base de datos (ajusta según tu formato)
    formato_fecha = "%Y-%m-%d"

    # Filtrar los préstamos vencidos
    prestamos_vencidos = []
    for prestamo in prestamos:
        try:
            # Convertir la fecha de devolución estimada (cadena) a un objeto de tipo date
            f_devolucion_estimada = datetime.strptime(prestamo.f_devolucion_estimada, formato_fecha).date()

            # Comparar las fechas
            if f_devolucion_estimada < fecha_actual:
                prestamos_vencidos.append(prestamo)
        except ValueError as e:
            print(f"Error al convertir la fecha del préstamo con ID {prestamo.id}: {e}")
            
    return prestamos_vencidos
