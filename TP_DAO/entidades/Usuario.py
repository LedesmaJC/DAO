class Usuario:
    def __init__(self, nombre, apellido, tipo, direccion, telefono):
        self.id = 0
        self.nombre = nombre
        self.apellido = apellido
        self.tipo = tipo
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"USUARIO--> ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Tipo: {self.tipo}, Direccion: {self.direccion}, Telefono: {self.telefono}"
    
