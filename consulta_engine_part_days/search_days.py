import json
from datetime import datetime, timedelta

# Variables
engine_part = 'parts.json'  # Nombre del archivo JSON a consultar
output_part = 'output_part_aviall.json'  # Nombre del archivo de salida
days = 90  # Cantidad de días a consultar

# Cargar el archivo JSON con codificación UTF-8
with open(engine_part, 'r', encoding='utf-8') as file:
    parts = json.load(file)

# Calcular la fecha de X días atrás (según la variable days)
days_ago = datetime.now() - timedelta(days=days)

# Filtrar y extraer datos relevantes
results = []

for part in parts:
    # Obtener la fecha actualizada del campo updatedAt
    updated_at_str = part['updatedAt']['$date']
    
    # Convertir la cadena de fecha a un objeto datetime
    updated_at = datetime.strptime(updated_at_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    
    # Verificar si la parte fue actualizada en los últimos X días
    if updated_at >= days_ago:
        # Encontrar el precio más reciente en quotes
        if part['quotes']:
            recent_price = max(part['quotes'], key=lambda x: int(x['createdAt']))['price']
        else:
            recent_price = None

        # Encontrar el stock en la primera ubicación (esto asume que el stock es el mismo en todas las ubicaciones)
        stock = part['location'][0]['stock'] if part['location'] else None
        
        # Agregar el resultado con los campos deseados
        results.append({
            'partNumberUnpunctuated': part.get('partNumberUnpunctuated'),
            'price': recent_price,
            'stock': stock,
            'updatedAt': updated_at_str,
            'imgUrl': part.get('imgUrl')  # Agregar imgUrl
        })

# Mostrar el número de archivos encontrados
print(f'Número de partes encontradas que cumplen con los criterios: {len(results)}')

# Guardar los resultados en un archivo JSON de salida
with open(output_part, 'w', encoding='utf-8') as output_file:
    json.dump(results, output_file, indent=4)

print(f'Resultados guardados en {output_part}')
