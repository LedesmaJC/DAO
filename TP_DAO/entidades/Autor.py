class Autor:
    def __init__(self, nombre, apellido, nacionalidad):
        self.id = 0
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"AUTOR--> ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Nacionalidad: {self.nacionalidad}"


