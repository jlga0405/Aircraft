import json

# Variables
vendor_file1 = 'vendor_file1.json'
list_correr = 'list_correr.json'
output_file = 'output_file.json'

# Cargar los archivos JSON
with open(vendor_file1, 'r') as vf:
    vendor_data = json.load(vf)

with open(list_correr, 'r') as lc:
    correr_list = json.load(lc)

# Obtener los partNumbers de list_correr
part_numbers_to_match = {item['partNumber'] for item in correr_list}

# Filtrar los elementos de vendor_file1 que tengan partNumber en list_correr
filtered_data = [item for item in vendor_data if item['partNumber'] in part_numbers_to_match]

# Guardar la salida en output_file
with open(output_file, 'w') as of:
    json.dump(filtered_data, of, indent=4)

print(f'Datos filtrados guardados en {output_file}')
