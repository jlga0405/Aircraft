import json

# Cargar el contenido de los archivos JSON
with open('artex.json', 'r') as f:
    artex_data = json.load(f)

with open('inv_airpart.json', 'r') as f:
    inv_airpart_data = json.load(f)

# Extraer los 'partNumber' de artex.json
partnumbers_artex = set(entry['partNumber'] for entry in artex_data)

# Inicializar una lista para almacenar los 'partNumber' eliminados
partnumbers_eliminados = []

# Iterar sobre las entradas de inv_airpart.json
for entry in inv_airpart_data:
    if entry['partNumber'] in partnumbers_artex:
        # Si el 'partNumber' está en artex.json, agregarlo a la lista de eliminados
        partnumbers_eliminados.append(entry['partNumber'])

# Eliminar los 'partNumber' presentes en artex.json de inv_airpart.json
inv_airpart_data = [entry for entry in inv_airpart_data if entry['partNumber'] not in partnumbers_artex]

# Guardar los cambios en inv_airpart_modif.json
with open('inv_airpart_modif.json', 'w') as f:
    json.dump(inv_airpart_data, f, indent=2)

# Guardar los 'partNumber' eliminados en eliminados.txt
with open('eliminados.txt', 'w') as f:
    for partnumber in partnumbers_eliminados:
        f.write(partnumber + '\n')

print("Proceso completado. Archivos generados: inv_airpart_modif.json y eliminados.txt")
