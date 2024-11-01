from reportlab.lib.pagesizes import  A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
def crear_pdf(datos):
    # Crear un documento PDF
    doc = SimpleDocTemplate("reporte.pdf", pagesize=A4)

    # Crear una lista para almacenar los elementos del informe
    elements = []

    # Crear estilos para el informe
    styles = getSampleStyleSheet()

    # Agregar un título
    title = "Reporte de usuarios con mas prestamos"
    elements.append(Paragraph(title, styles['Title']))

    # Agregar un párrafo de textogetSampleStyleSheet
    text = "En base al valor pasado por parámetro, se listan los usuarios con esa cantidad o más"
    elements.append(Paragraph(text, styles['Normal']))

    # Agregar una tabla de ejemplo
    data = [['Usuario', 'Cantidad de préstamos']]
    for usuario in datos:
        data.append([usuario[0], usuario[1]])
    table = Table(data, colWidths=[3 * inch, 2 * inch])
    # Estilos de la tabla
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Color de fondo para los encabezados
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Color del texto en los encabezados
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinear el texto al centro
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fuente en negrita para los encabezados
        ('FONTSIZE', (0, 0), (-1, 0), 12),  # Tamaño de fuente ajustado para los encabezados
        ('FONTSIZE', (0, 1), (-1, -1), 10),  # Tamaño de fuente ajustado para el contenido
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espaciado inferior en encabezados
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Fondo para las filas de la tabla
        ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Líneas de la cuadrícula
    ]))
    elements.append(Spacer(10, 10))
    elements.append(table)

    # Construir el informe y guardar en un archivo PDF
    doc.build(elements)