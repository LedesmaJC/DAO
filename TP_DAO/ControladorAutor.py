import sqlite3

# Conectar a la base de datos
def conectar_base_datos():
    try:
        connection = sqlite3.connect('TPI_DAO.db')
        return connection
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

# Guardar los datos del autor en la base de datos
def guardar_autor(autor):
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute(
                """
                INSERT INTO autores (nombre, apellido, nacionalidad)
                VALUES (?, ?, ?)
                """, 
                (autor.nombre, autor.apellido, autor.nacionalidad)
            )
            conexion.commit()
            print("Autor guardado correctamente.")
        except sqlite3.Error as e:
            print(f"Error durante la inserción: {e}")
        finally:
            cursor.close()
            conexion.close()
    else:
        print("No se pudo realizar la operación por problemas de conexión.")
        
# Obtener todos los autores para el Combobox
def obtener_autores():
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, apellido FROM autores")
            autores = cursor.fetchall()  # Retorna una lista de tuplas (id, nombre, apellido)
            return autores
        except sqlite3.Error as e:
            print(f"Error al obtener autores: {e}")
        finally:
            cursor.close()
            conexion.close()
    return []



# Obtener el ID del autor basado en el nombre completo
def obtener_id_autor(nombre_completo):
    conexion = conectar_base_datos()
    if conexion:
        try:
            cursor = conexion.cursor()
            nombre, apellido = nombre_completo.split(" ")  # Asumiendo que el nombre está en formato "Nombre Apellido"
            cursor.execute("SELECT id FROM autores WHERE nombre=? AND apellido=?", (nombre, apellido))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except sqlite3.Error as e:
            print(f"Error al obtener el ID del autor: {e}")
            return None
        finally:
            cursor.close()
            conexion.close()
    return None


