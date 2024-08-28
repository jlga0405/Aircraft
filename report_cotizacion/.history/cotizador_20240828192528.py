import json
import pandas as pd

# Variables
valor = 0.65
file = 'productos.json'  

# Cargar el archivo JSON
with open(file, 'r') as f:
    productos = json.load(f)

# Procesar los datos y agregar el campo 'priceventa'
for producto in productos:
    if producto['productprice'] > 0:  # Asegurarse de que el precio sea mayor que 0
        producto['priceventa'] = producto['productprice'] / valor
    else:
        producto['priceventa'] = 0  # Si el precio es 0, el precio de venta también será 0

# Convertir a DataFrame
df = pd.DataFrame(productos)

# Guardar en un archivo XLSX
df.to_excel('productos_con_priceventa.xlsx', index=False)

print("El archivo 'productos_con_priceventa.xlsx' ha sido creado exitosamente.")
