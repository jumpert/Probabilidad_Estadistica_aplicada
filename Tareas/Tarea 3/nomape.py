import openpyxl
import random

# Generar 10,000 números de documentos aleatorios sin repetir entre 1 millón y 6 millones
documentos = random.sample(range(1000000, 6000001), 10000)

# Crear un nuevo archivo Excel
wb = openpyxl.Workbook()
sheet = wb.active

# Agregar encabezado a la columna
sheet['A1'] = 'Número de Documento'

# Agregar los números de documentos a las filas
for i, documento in enumerate(documentos, start=2):
    sheet[f'A{i}'] = documento

# Guardar el archivo Excel
wb.save('numeros_documentos.xlsx')