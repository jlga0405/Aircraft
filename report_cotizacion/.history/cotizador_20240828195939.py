import json
import pandas as pd

# Variables
valor = 0.65
file = 'productos.json'  # Nombre del archivo JSON de entrada
outputfile = 'productos_con_priceventa.xlsx'  # Nombre del archivo XLSX de salida
multiply = True  # Si es True, multiplica; si es False, divide

# Cargar el archivo JSON
with open(file, 'r') as f:
    productos = json.load(f)

# Procesar los datos y agregar el campo 'priceventa' con dos decimales
for producto in productos:
    if producto['productprice'] > 0:  # Asegurarse de que el precio sea mayor que 0
        if multiply:
            producto['priceventa'] = round(producto['productprice'] * valor, 2)
        else:
            producto['priceventa'] = round(producto['productprice'] / valor, 2)
    else:
        producto['priceventa'] = 0  # Si el precio es 0, el precio de venta también será 0

# Convertir a DataFrame
df = pd.DataFrame(productos)

# Guardar en un archivo XLSX
df.to_excel(outputfile, index=False)

print(f"El archivo '{outputfile}' ha sido creado exitosamente.")
