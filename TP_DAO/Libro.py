class Libro:
    def __init__(self, isbn, titulo, genero, anioPublicacion, autor, stock):
        self.isbn = isbn
        self.titulo = titulo
        self.genero = genero
        self.anioPublicacion = anioPublicacion
        self.autor = autor
        self.stock = stock

    def __str__(self):
        return f"Libro--> ISBN: {self.isbn}, Titulo: {self.titulo}, Genero: {self.genero}, Año de Publicacion: {self.anioPublicacion}, Autor: {self.autor}, Stock: {self.stock}"
    

