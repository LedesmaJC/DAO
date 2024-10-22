class Prestamo:
    def __init__(self, id, usuario , libro, fechaPrestamo, fechaDevolucion):
        self.id = id
        self.usuario = usuario
        self.libro = libro
        self.fechaPrestamo = fechaPrestamo
        self. fechaDevolucion = fechaDevolucion

    def __str__(self):
        return f"PRESTAMO--> ID: {self.id}, Usuario: {self.usuario}, Libro: {self.libro}, Fecha de Prestamo: {self.fechaPrestamo}, Fecha de Devolucion: {self.fechaDevolucion}"
