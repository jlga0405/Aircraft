import json
import pandas as pd


stock_file = 'Inventario_stock_Quantum_26092024.json'
inventario_file = 'Lista_inventario_26092024.json'
output_file = 'reporte_Inv_Quatum.xlsx'


with open(stock_file, 'r') as f:
    stock_data = json.load(f)

with open(inventario_file, 'r') as f:
    inventario_data = json.load(f)

# Procesar los datos de stock para sumar el stock por productcode
stock_summary = {}
duplicated_codes = set()
for item in stock_data:
    code = str(item['productcode'])
    try:
        stock = int(item['stock'])
    except ValueError:
        print(f"Advertencia: El valor de stock '{item['stock']}' para el productcode '{code}' no es un número entero válido.")
        continue

    if code in stock_summary:
        stock_summary[code] += stock
        duplicated_codes.add(code)
    else:
        stock_summary[code] = stock

# Obtener los productcode de inventario
inventario_codes = {item['productcode'] for item in inventario_data}

# Filtrar los duplicados que están en inventario_file
filtered_duplicated_codes = duplicated_codes.intersection(inventario_codes)

# Imprimir los productcode duplicados que están en inventario_file
if filtered_duplicated_codes:
    print("Productcodes duplicados en stock_file y presentes en inventario_file:")
    for code in filtered_duplicated_codes:
        print(f"{code}: {stock_summary[code]}")

# Filtrar y preparar los datos para el archivo de salida
output_data = []
for item in inventario_data:
    code = item['productcode']
    price = item['productprice']
    stock = stock_summary.get(code, 0)  # Obtener stock, 0 si no existe
    
    output_data.append({
        'productcode': code,
        'productprice': price,
        'stock': stock
    })

# Convertir la lista a un DataFrame de pandas y guardarla como un archivo Excel
df = pd.DataFrame(output_data)
df = df.drop_duplicates(subset='productcode')  # Asegurarse de tener solo un `productcode` por fila
df.to_excel(output_file, index=False)

print(f'Archivo de salida generado: {output_file}')
