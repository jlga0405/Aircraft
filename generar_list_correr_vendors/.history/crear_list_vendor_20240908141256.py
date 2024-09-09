import json

# Variables
vendor_file1 = 'Aviall_General.json'
list_correr = 'Lista_1878_07092024_01.json'
output_file = 'output_Lista_1878_07092024_01.json'
nofound_file = 'partNumberNofound.txt'

# Cargar los archivos JSON
with open(vendor_file1, 'r') as vf:
    vendor_data = json.load(vf)

with open(list_correr, 'r') as lc:
    correr_list = json.load(lc)

# Crear un diccionario para convertir partNumbers de vendor_file1 (sin guiones)
vendor_data_cleaned = {item['partNumber'].replace('-', ''): item for item in vendor_data}

# Variables para los resultados
filtered_data = []
nofound_part_numbers = []

# Iterar sobre los partNumbers en list_correr
for correr_item in correr_list:
    correr_partNumber_cleaned = correr_item['partNumber'].replace('-', '')
    
    # Buscar en vendor_data_cleaned
    if correr_partNumber_cleaned in vendor_data_cleaned:
        # Recuperar el producto y agregar solo los campos partNumber y url, con el partNumber de list_correr
        product = vendor_data_cleaned[correr_partNumber_cleaned]
        filtered_data.append({
            'partNumber': correr_item['partNumber'],  # Mantener formato original de list_correr
            'url': product['url']
        })
    else:
        # Agregar a la lista de no encontrados
        nofound_part_numbers.append(correr_item['partNumber'])

# Guardar los resultados filtrados en output_file.json
with open(output_file, 'w') as of:
    json.dump(filtered_data, of, indent=4)

# Guardar los partNumbers no encontrados en partNumberNofound.txt
with open(nofound_file, 'w') as nf:
    for partNumber in nofound_part_numbers:
        nf.write(partNumber + '\n')

print(f'Datos filtrados guardados en {output_file}')
print(f'PartNumbers no encontrados guardados en {nofound_file}')
