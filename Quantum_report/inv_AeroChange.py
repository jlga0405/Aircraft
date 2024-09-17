import pandas as pd
import json

# Definir los archivos de entrada y salida (en la misma ruta que el script)
in_file = "Inventario al corte 13 septiembre 2024.json"  # Archivo de entrada (JSON)
out_file = "AeroChange_grouped.xlsx"  # Archivo de salida (Excel)

# Cargar el archivo JSON
with open(in_file, 'r') as file:
    data = json.load(file)

# Convertir el JSON a un DataFrame de pandas
df = pd.DataFrame(data)

# Verifica los tipos de datos de cada columna
print(df.dtypes)

# Convertir la columna 'Qty Avl' a numérica, invalidando los no numéricos
df['Qty Avl'] = pd.to_numeric(df['Qty Avl'], errors='coerce')

# Eliminar filas donde 'Qty Avl' no es numérico (es decir, es NaN)
df = df.dropna(subset=['Qty Avl'])

# Asegurarse de que las columnas utilizadas para agrupar sean de tipo string
df['Part Number'] = df['Part Number'].astype(str)
df['Part Description'] = df['Part Description'].astype(str)
df['Cond'] = df['Cond'].astype(str)

# Agrupar los datos por las columnas 'Part Number', 'Part Description' y 'Cond', sumando la columna 'Qty Avl'
df_grouped = df.groupby(['Part Number', 'Part Description', 'Cond'], as_index=False).agg({'Qty Avl': 'sum'})

# Verifica el resultado de la agrupación
print(df_grouped)

# Guardar el resultado en un archivo Excel
df_grouped.to_excel(out_file, index=False)

print(f"Proceso completado. El archivo ha sido guardado en {out_file}.")
