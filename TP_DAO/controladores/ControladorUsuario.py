import sqlite3
from entidades.Usuario import Usuario

from datos.DBConnection import DBConnection

# Instanciamos el singleton
db = DBConnection('datos/TPI_DAO.db')

# Obtenemos la conexión
connection = db.get_connection()
# Obtener todos los usuarios de la base de datos
def obtener_usuarios():
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuarios")  
            usuarios = cursor.fetchall()
            if usuarios:
                lista_usuarios = []
                for usuario in usuarios:
                    u = Usuario(
                        nombre = usuario[1], 
                        apellido= usuario[2], 
                        tipo= usuario[3], 
                        direccion= usuario[4], 
                        telefono= usuario[5]
                    )
                    u.id= usuario[0]
                    lista_usuarios.append(u)
            return lista_usuarios
        except sqlite3.Error as e:
            print(f"Error al obtener usuarios: {e}")
            return []
        finally:
            if cursor:  # Solo cerramos el cursor si fue creado
                cursor.close()
    else:
        print("No se pudo conectar a la base de datos.")
        return []
    

# Guardar los datos del usuario en la base de datos
def guardar_usuario(usuario):
    if connection:
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO usuarios (nombre, apellido, tipo, direccion, telefono)
                VALUES (?, ?, ? , ?, ?)
                """, 
                (usuario.nombre, usuario.apellido, usuario.tipo, usuario.direccion, usuario.telefono)
            )
            connection.commit()
            print("Usuario guardado correctamente.")
        except sqlite3.IntegrityError as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        except sqlite3.Error as e:
            raise Exception("Error durante la inserción: " + str(e))  # Lanza la excepción para manejar en la GUI
        finally:
            if cursor:  # Solo cerramos el cursor si fue creado
                cursor.close()
    else:
        raise Exception("No se pudo realizar la operación por problemas de conexión.")
