import sqlite3

class DBConnection:
    _instance = None
    dbconnection = None

    def __new__(cls, connection_string: str):
        if not cls._instance:
            cls._instance = super(DBConnection, cls).__new__(cls)
            try:
                # Intentar conectar con la base de datos
                cls.dbconnection = sqlite3.connect(connection_string)
                print("Conexión exitosa a la base de datos")
            except sqlite3.Error as e:
                print(f"Error al conectar a la base de datos: {e}")
                cls.dbconnection = None
        return cls._instance
    #Conexión de la BD
    def get_connection(self):
        return self.dbconnection

db = DBConnection('datos/TPI_DAO.db')
connection = db.get_connection()

if connection:
    print("Base de datos conectada correctamente.")
else:
    print("No se pudo conectar a la base de datos.")
