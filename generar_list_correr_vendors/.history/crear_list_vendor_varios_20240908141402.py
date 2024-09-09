import json
import os

# Variables
vendor_files = [
    'Aviall_General.json',
    'wencor_General.json',
    'airparts_General.json',
    'klx_General.json',
    'proponent_General.json',
    'incorashop_General.json'
]
list_correr = 'Lista_1878_07092024_01.json'
nofound_file_template = 'partNumberNofound_{}.txt'  # Plantilla para archivos no encontrados
output_file_template = 'output_Lista_Agregar_{}.json'  # Plantilla para archivos de salida

# Cargar la lista de correr
with open(list_correr, 'r') as lc:
    correr_list = json.load(lc)

# Iterar sobre cada vendor_file y procesarlo
for vendor_file in vendor_files:
    # Extraer el nombre del proveedor (ej. 'aviall' de 'Aviall_General.json')
    vendor_name = vendor_file.split('_')[0].lower()

    # Crear el directorio si no existe
    os.makedirs(vendor_name, exist_ok=True)

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
        # Convertir el partNumber a cadena si no lo es y aplicar replace
        correr_partNumber_cleaned = str(correr_item['partNumber']).replace('-', '')

        # Buscar en vendor_data_cleaned
        if correr_partNumber_cleaned in vendor_data_cleaned:
            # Recuperar el producto
            product = vendor_data_cleaned[correr_partNumber_cleaned]

            # Si la clave 'url' no está presente, asignar None (equivalente a null en JSON)
            url_value = product.get('url', None)

            # Agregar a los datos filtrados
            filtered_data.append({
                'partNumber': correr_item['partNumber'],  # Mantener formato original de list_correr
                'url': url_value
            })
        else:
            # Agregar a la lista de no encontrados
            nofound_part_numbers.append(correr_item['partNumber'])

    # Definir las rutas de los archivos de salida dentro de la carpeta del proveedor
    output_file = os.path.join(vendor_name, output_file_template.format(vendor_name))
    nofound_file = os.path.join(vendor_name, nofound_file_template.format(vendor_name))

    # Guardar los resultados filtrados en el archivo output para el proveedor actual
    with open(output_file, 'w') as of:
        json.dump(filtered_data, of, indent=4)

    # Guardar los partNumbers no encontrados en el archivo nofound para el proveedor actual
    with open(nofound_file, 'w') as nf:
        for partNumber in nofound_part_numbers:
            nf.write(str(partNumber) + '\n')

    print(f'Datos filtrados guardados en {output_file}')
    print(f'PartNumbers no encontrados guardados en {nofound_file}')
