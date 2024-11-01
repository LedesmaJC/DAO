class Prestamo:
        
    def __init__(self, usuario , libro, f_prestamo, f_devolucion_estimada):
        self.id = 0
        self.usuario = usuario
        self.libro = libro
        self.f_prestamo = f_prestamo
        self.f_devolucion_estimada = f_devolucion_estimada
        self.f_devolucion_real = ""
        self.observacion = ""
        
    def __str__(self):
        return f"PRESTAMO--> ID: {self.id}, Usuario: {self.usuario}, Libro: {self.libro}, Fecha de Prestamo: {self.fechaPrestamo}, Fecha de Devolucion: {self.fechaDevolucion}"
