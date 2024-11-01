from reportlab.lib.pagesizes import  A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

# Crear un documento PDF
doc = SimpleDocTemplate("report.pdf", pagesize=A4)

# Crear una lista para almacenar los elementos del informe
elements = []

# Crear estilos para el informe
styles = getSampleStyleSheet()

# Agregar un título
title = "Ejemplo de Informe PDF con ReportLab., hoy es 30/10"
elements.append(Paragraph(title, styles['Title']))

# Agregar un párrafo de textogetSampleStyleSheet
text = "Este es un informe de ejemplo generado con ReportLab en Python."
elements.append(Paragraph(text, styles['Normal']))

# Agregar una tabla de ejemplo
data = [["Nombre", "Edad", "Ciudad"],
        ["Juan", "25", "Madrid"],
        ["María", "30", "Barcelona"]]
table = Table(data, colWidths=[1 * inch, 0.5 * inch, 1 * inch])
table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                          ('TEXTCOLOR', (0, 0), (-1, 0), colors.lightblue),
                          ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                          ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                          ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                          ('BACKGROUND', (0, 1), (-1, -1), colors.yellow),
                          ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
elements.append(Spacer(10, 10))
elements.append(table)

# Construir el informe y guardar en un archivo PDF
doc.build(elements)
