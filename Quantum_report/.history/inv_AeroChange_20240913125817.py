import pandas as pd

# Definir los archivos de entrada y salida (en la misma ruta que el script)
in_file = "Inventario al corte 13 septiembre 2024.xlsx"  # Archivo de entrada
out_file = "AeroChange_grouped.xlsx"  # Archivo de salida

# Cargar el archivo Excel
df = pd.read_excel(in_file)

# Verifica los tipos de datos de cada columna
print(df.dtypes)

# Convertir la columna 'Qty Avl' a numérica, invalidando los no numéricos
df['Qty Avl'] = pd.to_numeric(df['Qty Avl'], errors='coerce')

# Eliminar filas donde 'Qty Avl' no es numérico (es decir, es NaN)
df = df.dropna(subset=['Qty Avl'])

# Agrupar los datos por las columnas 'Part Number', 'Part Description' y 'Cond', sumando la columna 'Qty Avl'
df_grouped = df.groupby(['Part Number', 'Part Description', 'Cond'], as_index=False).agg({'Qty Avl': 'sum'})

# Verifica el resultado de la agrupación
print(df_grouped)

# Guardar el resultado en un archivo Excel
df_grouped.to_excel(out_file, index=False)

print(f"Proceso completado. El archivo ha sido guardado en {out_file}.")
