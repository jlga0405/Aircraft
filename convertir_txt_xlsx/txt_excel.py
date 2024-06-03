import pandas as pd
import re

# Definir las variables para los nombres de los archivos
archivo_input = 'INVENTARIOJUNE2024.txt'
archivo_output = 'INVENTARIOJUNE2024.xlsx'

# Definir una función para procesar cada línea del archivo de texto
def procesar_linea(linea):
    # Usar una expresión regular para dividir por espacios múltiples
    return re.split(r'\s{2,}', linea.strip())

# Leer el archivo de texto línea por línea
with open(archivo_input, 'r') as file:
    lineas = file.readlines()

# Procesar cada línea
datos_procesados = [procesar_linea(linea) for linea in lineas]

# Convertir a DataFrame
df = pd.DataFrame(datos_procesados, columns=[
    'Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 'Col8'])

# Escribir el DataFrame a un archivo Excel
df.to_excel(archivo_output, index=False)

print(f'Archivo convertido y guardado en: {archivo_output}')
