import pandas as pd

# Cargar el archivo Excel
in_file = "path_to_your_file.xlsx"  # Reemplaza con la ruta real de tu archivo
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
out_file = "path_to_output_file.xlsx"  # Reemplaza con la ruta real del archivo de salida
df_grouped.to_excel(out_file, index=False)

print("Proceso completado y archivo guardado.")
