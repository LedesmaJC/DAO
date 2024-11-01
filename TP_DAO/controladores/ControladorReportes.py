import controladores.ControladorPrestamo as c_p
import controladores.ControladorUsuario as c_u
import controladores.GeneradorPDF as pdf


def reporte_uno():
    return c_p.buscar_vencidos()

def reporte_dos():
    pass

def reporte_tres(param):
    lista_prestamos = c_p.buscar_todos()
    lista_usuarios = c_u.obtener_usuarios()
    lista_nombre = []
    cantidad = 0
    for i in range(len(lista_usuarios)):
        usuario_nombre = lista_usuarios[i].nombre
        usuario_apellido = lista_usuarios[i].apellido
        for prestamo in lista_prestamos:
            if prestamo.usuario == f"{usuario_nombre} {usuario_apellido}":
                cantidad += 1
        if cantidad >= int(param):
            lista_nombre.append((f"{usuario_nombre} {usuario_apellido}", cantidad))
        cantidad = 0
    print(lista_nombre)
    pdf.crear_pdf(lista_nombre)