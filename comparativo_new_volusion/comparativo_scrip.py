import json

# Cargar el contenido de los archivos JSON
with open('archivo_inv.json', 'r') as f:
    archivo_inv_data = json.load(f)

with open('archivo_lista.json', 'r') as f:
    archivo_lista_data = json.load(f)

# Extraer los 'partNumber' de archivo_inv.json
part_numbers_archivo_inv = set(entry['partNumber'] for entry in archivo_inv_data)

# Extraer los 'partNumber' de archivo_lista.json
part_numbers_archivo_lista = set(entry['partNumber'] for entry in archivo_lista_data)

# Encontrar los 'partNumber' que están en archivo_lista.json pero no en archivo_inv.json
part_numbers_eliminados = part_numbers_archivo_lista.intersection(part_numbers_archivo_inv)

# Filtrar las entradas de archivo_inv_data para mantener solo los 'partNumber' presentes en archivo_lista_data
archivo_inv_data = [entry for entry in archivo_inv_data if entry['partNumber'] not in part_numbers_eliminados]

# Guardar el resultado actualizado en archivo_inv.json
with open('archivo_inv.json', 'w') as f:
    json.dump(archivo_inv_data, f, indent=2)

# Mostrar los 'partNumber' eliminados en pantalla
print("PartNumber eliminados del archivo 'archivo_inv.json':")
for part_number in part_numbers_eliminados:
    print(part_number)

# Guardar los 'partNumber' eliminados en un archivo JSON llamado 'eliminados.json'
eliminados_data = [{'partNumber': part_number} for part_number in part_numbers_eliminados]
with open('eliminados.json', 'w') as f:
    json.dump(eliminados_data, f, indent=2)

print("Comparación completada. Archivo 'archivo_inv.json' actualizado.")
