import json

# Variables para los archivos
datavolusion_file = 'Data_Volusion.json'
engineparts_file = 'parts.json'
fileoutput_file = 'output_result.json'

# Cargar los datos de los archivos JSON con codificación utf-8
with open(datavolusion_file, 'r', encoding='utf-8') as f:
    datavolusion_data = json.load(f)

with open(engineparts_file, 'r', encoding='utf-8') as f:
    engineparts_data = json.load(f)

# Crear un diccionario para buscar los datos de engineparts por partNumberUnpunctuated
engineparts_dict = {}
for part in engineparts_data:
    part_number_unpunctuated = part.get('partNumberUnpunctuated')
    url = part.get('url')
    if part_number_unpunctuated and url:
        engineparts_dict[part_number_unpunctuated] = url

# Crear una lista para almacenar los resultados
results = []

# Comparar los partNumbers y encontrar los matches
for part in datavolusion_data:
    part_number = str(part['partNumber'])  # Asegurarse de que sea una cadena
    # Quitar caracteres especiales y guiones bajos del partNumber para que coincida con partNumberUnpunctuated
    part_number_cleaned = part_number.replace('-', '').replace('_', '')
    if part_number_cleaned in engineparts_dict:
        url = engineparts_dict[part_number_cleaned]
        results.append({
            'partNumber': part_number,
            'url': url
        })
        # Mostrar en pantalla el partNumber y la URL encontrados
        print(f"Encontrado: partNumber = {part_number}, URL = {url}")

# Guardar los resultados en un archivo JSON
with open(fileoutput_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=4)

# Mostrar el total de resultados encontrados
total_found = len(results)
print(f"Total de partNumbers encontrados: {total_found}")
print(f"Los resultados se han guardado en {fileoutput_file}")
