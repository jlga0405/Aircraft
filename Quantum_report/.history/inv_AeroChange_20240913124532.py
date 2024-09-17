import pandas as pd

# Variables de entrada y salida
in_file = 'Inventario al corte 13 septiembre 2024.xlsx'  # Nombre del archivo de entrada
output_file = 'INV_AeroChange_Sep13_2024.xlsx'  # Nombre del archivo de salida

# Leer archivo Excel
df = pd.read_excel(in_file)

# Agrupar por 'Part Number' y sumar 'Qty Avl'
df_grouped = df.groupby(['Part Number', 'Part Description', 'Cond'], as_index=False).agg({'Qty Avl': 'sum'})

# Guardar el resultado en un nuevo archivo Excel
df_grouped.to_excel(output_file, index=False)

print(f"Archivo {output_file} generado exitosamente.")
