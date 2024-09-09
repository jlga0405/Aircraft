import json
import os

# Variables
list_correr = 'Lista_1878_07092024_04.json'

# Extraer el número final de list_correr (antes de la extensión .json)
# Se asume que el formato siempre es algo como 'Lista_1878_07092024_XX.json'
numero_final = list_correr.split('_')[-1].replace('.json', '')

# Modificar las plantillas para incluir el número final
nofound_file_template = f'partNumberNofound_{numero_final}_{{}}.txt'
output_file_template = f'output_Lista_1878_07092024_{numero_final}_{{}}.json'

# Resto del código permanece igual...
# Lista de archivos de proveedores
vendor_files = [
    'Aviall_General.json',
    'wencor_General.json',
    'airparts_General.json',
    'klx_General.json',
    'proponent_General.json',
    'incorashop_General.json'
]

# Cargar la lista de correr
with open(list_correr, 'r') as lc:
    correr_list = json.load(lc)

# Iterar sobre cada vendor_file y procesarlo
for vendor_file in vendor_files:
    # Cargar el archivo JSON del proveedor actual
    with open(vendor_file, 'r') as vf:
        vendor_data = json.load(vf)

    # Crear un diccionario para convertir partNumbers de vendor_file (sin guiones)
    vendor_data_cleaned = {item['partNumber'].replace('-', ''): item for item in vendor_data}

    # Variables para los resultados
    filtered_data = []
    nofound_part_numbers = []

    # Iterar sobre los partNumbers en list_correr
    for correr_item in correr_list:
        correr_partNumber_cleaned = correr_item['partNumber'].replace('-', '')

        # Buscar en vendor_data_cleaned
        if correr_partNumber_cleaned in vendor_data_cleaned:
            product = vendor_data_cleaned[correr_partNumber_cleaned]
            filtered_data.append({
                'partNumber': correr_item['partNumber'],  # Mantener formato original de list_correr
                'url': product.get('url', None)  # Usar None si no existe 'url'
            })
        else:
            nofound_part_numbers.append(correr_item['partNumber'])

    # Guardar los resultados filtrados en un archivo output para el proveedor actual
    output_file = output_file_template.format(vendor_file.split('_')[0])
    with open(output_file, 'w') as of:
        json.dump(filtered_data, of, indent=4)

    # Guardar los partNumbers no encontrados en un archivo nofound para el proveedor actual
    nofound_file = nofound_file_template.format(vendor_file.split('_')[0])
    with open(nofound_file, 'w') as nf:
        for partNumber in nofound_part_numbers:
            nf.write(str(partNumber) + '\n')

    print(f'Datos filtrados guardados en {output_file}')
    print(f'PartNumbers no encontrados guardados en {nofound_file}')
