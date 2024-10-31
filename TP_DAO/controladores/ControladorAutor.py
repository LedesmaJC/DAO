import sqlite3

from datos.DBConnection import DBConnection

# Instanciamos el singleton
db = DBConnection('datos/TPI_DAO.db')

# Obtenemos la conexión
connection = db.get_connection()

# Guardar los datos del autor en la base de datos
def guardar_autor(autor):
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO autores (nombre, apellido, nacionalidad)
                VALUES (?, ?, ?)
                """, 
                (autor.nombre, autor.apellido, autor.nacionalidad)
            )
            connection.commit()
            print("Autor guardado correctamente.")
        except sqlite3.Error as e:
            print(f"Error durante la inserción: {e}")
        finally:
            cursor.close()
            connection.close()
    else:
        print("No se pudo realizar la operación por problemas de conexión.")
        
# Obtener todos los autores para el Combobox
def obtener_autores():
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id, nombre, apellido FROM autores")
            autores = cursor.fetchall()  # Retorna una lista de tuplas (id, nombre, apellido)
            return autores
        except sqlite3.Error as e:
            print(f"Error al obtener autores: {e}")
        finally:
            if cursor:  # Solo cerramos el cursor si fue creado
                cursor.close()
    return []



# Obtener el ID del autor basado en el nombre completo
def obtener_id_autor(nombre_completo):
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()
            nombre, apellido = nombre_completo.split(" ")  # Asumiendo que el nombre está en formato "Nombre Apellido"
            cursor.execute("SELECT id FROM autores WHERE nombre=? AND apellido=?", (nombre, apellido))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except sqlite3.Error as e:
            print(f"Error al obtener el ID del autor: {e}")
            return None
        finally:
            if cursor:  # Solo cerramos el cursor si fue creado
                cursor.close()
    return None


