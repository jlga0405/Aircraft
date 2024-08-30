import json
import pandas as pd

# Variables
file = 'productos.json'  # Nombre del archivo JSON de entrada
cotizacion_file = 'cotizacion.json'  # Nombre del archivo JSON de cotización
outputfile = 'List_Cotizador.xlsx'  # Nombre del archivo XLSX de salida

# Cargar los archivos JSON
with open(file, 'r') as f:
    productos = json.load(f)

with open(cotizacion_file, 'r') as f:
    cotizacion = json.load(f)

# Crear un diccionario para acceder a los productos por 'produtCode'
productos_dict = {prod['produtCode']: prod for prod in productos}

# Procesar los datos y calcular el precio sugerido
for cot in cotizacion:
    prod_code = cot['produtCode']
    cantidad = cot['cantidad']

    if prod_code in productos_dict:
        producto = productos_dict[prod_code]
        stock = producto['stock']
        precio_base = producto['productPrice']
        
        # Determinar la cantidad a usar para el cálculo
        if cantidad > stock:
            cantidad_calculo = stock
            comentario = 'Calculo basado en stock'
        else:
            cantidad_calculo = cantidad
            comentario = 'Calculo basado en cantidad'
        
        # Calcular el precio sugerido basado en la cantidad_calculo
        if 0 <= cantidad_calculo <= 1999:
            precio_sugerido = round(precio_base * 1.45, 2)
            calculo_aplicado = '1.45'
        elif 2000 <= cantidad_calculo <= 5000:
            precio_sugerido = round(precio_base * 0.30, 2)
            calculo_aplicado = '0.30'
        elif 5001 <= cantidad_calculo <= 10000:
            precio_sugerido = round(precio_base * 1.32, 2)
            calculo_aplicado = '1.32'
        else:
            precio_sugerido = precio_base
            calculo_aplicado = 'N/A'
        
        # Asignar resultados al producto
        producto['cantidad'] = cantidad  # Agregar la cantidad del cotizador
        producto['PrecioSugerido'] = precio_sugerido
        producto['calculo_aplicado'] = calculo_aplicado
        producto['comentario'] = comentario

# Convertir a DataFrame
df = pd.DataFrame(productos)

# Guardar en un archivo XLSX
df.to_excel(outputfile, index=False)

print(f"El archivo '{outputfile}' ha sido creado exitosamente.")
