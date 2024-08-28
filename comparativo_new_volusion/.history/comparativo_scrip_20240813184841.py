import json

# Definir los nombres de los archivos
file_master = 'excludedList.json'  # Archivo maestro para comparar
file_in = 'Inventario_23072024.json'  # Archivo de entrada a comparar
file_output = 'archivo_salida.json'  # Archivo de salida para guardar los que están en file_in pero no en file_master

# Cargar el contenido de los archivos JSON
with open(file_master, 'r') as f:
    archivo_master_data = json.load(f)

with open(file_in, 'r') as f:
    archivo_in_data = json.load(f)

# Extraer los 'partNumber' de archivo_master.json y archivo_in.json
part_numbers_master = set(entry['partNumber'] for entry in archivo_master_data)
part_numbers_in = set(entry['partNumber'] for entry in archivo_in_data)

# Encontrar los 'partNumber' que están en archivo_in pero no en archivo_master
part_numbers_no_presentes_en_master = part_numbers_in - part_numbers_master

# Guardar los 'partNumber' que no están en file_master en el archivo de salida
eliminados_data = [{'partNumber': part_number} for part_number in part_numbers_no_presentes_en_master]
with open(file_output, 'w') as f:
    json.dump(eliminados_data, f, indent=2)

# Mostrar los 'partNumber' no presentes en file_master en pantalla
print(f"PartNumbers que están en '{file_in}' pero no en '{file_master}':")
for part_number in part_numbers_no_presentes_en_master:
    print(part_number)

print(f"Comparación completada. Los 'partNumber' no presentes en '{file_master}' se guardaron en '{file_output}'.")
