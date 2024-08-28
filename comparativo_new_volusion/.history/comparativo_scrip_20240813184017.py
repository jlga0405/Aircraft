import json

# Definir los nombres de los archivos
file_master = 'archivo_inv.json'  # Archivo maestro para comparar
file_in = 'archivo_lista.json'    # Archivo de entrada a comparar
file_output = 'archivo_salida.json'  # Archivo de salida para guardar los que no están en ninguno de los dos

# Cargar el contenido de los archivos JSON
with open(file_master, 'r') as f:
    archivo_master_data = json.load(f)

with open(file_in, 'r') as f:
    archivo_in_data = json.load(f)

# Extraer los 'partNumber' de archivo_master.json
part_numbers_master = set(entry['partNumber'] for entry in archivo_master_data)

# Extraer los 'partNumber' de archivo_in.json
part_numbers_in = set(entry['partNumber'] for entry in archivo_in_data)

# Encontrar los 'partNumber' que están en archivo_lista.json pero no en archivo_master.json
part_numbers_eliminados = part_numbers_in.intersection(part_numbers_master)

# Filtrar las entradas de archivo_master_data para mantener solo los 'partNumber' presentes en archivo_in_data
archivo_master_data = [entry for entry in archivo_master_data if entry['partNumber'] not in part_numbers_eliminados]

# Guardar el resultado actualizado en file_master (archivo_inv.json)
with open(file_master, 'w') as f:
    json.dump(archivo_master_data, f, indent=2)

# Guardar los 'partNumber' eliminados en el archivo de salida
eliminados_data = [{'partNumber': part_number} for part_number in part_numbers_eliminados]
with open(file_output, 'w') as f:
    json.dump(eliminados_data, f, indent=2)

# Mostrar los 'partNumber' eliminados en pantalla
print(f"PartNumber eliminados del archivo '{file_master}':")
for part_number in part_numbers_eliminados:
    print(part_number)

print(f"Comparación completada. Archivo '{file_master}' actualizado y los 'partNumber' eliminados se guardaron en '{file_output}'.")
