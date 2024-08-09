import json
from datetime import datetime, timedelta

# Variables
engine_part = 'parts.json'  # Nombre del archivo JSON a consultar
output_part = 'output_part_aviall.json'  # Nombre del archivo para partes actualizadas en los últimos 90 días
output_part_not = 'output_parts_notUpdate_aviall.json'  # Nombre del archivo para partes no actualizadas en los últimos 200 días
days_recent_update = 90  # Cantidad de días para partes actualizadas recientemente
days_without_changes = 200  # Cantidad de días sin cambios

# Cargar el archivo JSON con codificación UTF-8
with open(engine_part, 'r', encoding='utf-8') as file:
    parts = json.load(file)

# Fechas de umbral
days_ago_recent_update = datetime.now() - timedelta(days=days_recent_update)
threshold_date_no_update = datetime.now() - timedelta(days=days_without_changes)

# Filtrar y extraer datos relevantes para partes actualizadas recientemente
recent_updates = []
no_updates = []

for part in parts:
    # Obtener la fecha actualizada del campo updatedAt
    updated_at_str = part['updatedAt']['$date']
    
    # Convertir la cadena de fecha a un objeto datetime
    updated_at = datetime.strptime(updated_at_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    
    # Verificar si la parte fue actualizada en los últimos X días
    if updated_at >= days_ago_recent_update:
        # Encontrar el precio más reciente en quotes
        if part['quotes']:
            # Convertir el campo createdAt a int para comparar timestamps
            recent_price = max(part['quotes'], key=lambda x: int(x['createdAt']))['price']
        else:
            recent_price = None

        # Encontrar el stock en la primera ubicación (esto asume que el stock es el mismo en todas las ubicaciones)
        stock = part['location'][0]['stock'] if part['location'] else None
        
        # Agregar el resultado con los campos deseados
        recent_updates.append({
            'partNumberUnpunctuated': part.get('partNumberUnpunctuated'),
            'price': recent_price,
            'stock': stock,
            'updatedAt': updated_at_str,
            'imgUrl': part.get('imgUrl')  # Agregar imgUrl
        })
    
    # Verificar si la parte no ha sido actualizada en los últimos X días
    if updated_at < threshold_date_no_update:
        # Encontrar el precio más reciente en quotes
        if part['quotes']:
            # Convertir el campo createdAt a int para comparar timestamps
            recent_price = max(part['quotes'], key=lambda x: int(x['createdAt']))['price']
        else:
            recent_price = None

        # Encontrar el stock en la primera ubicación (esto asume que el stock es el mismo en todas las ubicaciones)
        stock = part['location'][0]['stock'] if part['location'] else None
        
        # Agregar el resultado con los campos deseados
        no_updates.append({
            'partNumberUnpunctuated': part.get('partNumberUnpunctuated'),
            'price': recent_price,
            'stock': stock,
            'updatedAt': updated_at_str,
            'imgUrl': part.get('imgUrl')  # Agregar imgUrl
        })

# Mostrar resultados
total_parts = len(parts)
num_recent_updates = len(recent_updates)
num_no_updates = len(no_updates)

print(f'Número total de partes comparadas: {total_parts}')
print(f'Número de partes actualizadas en los últimos {days_recent_update} días: {num_recent_updates}')
print(f'Número de partes sin cambios en los últimos {days_without_changes} días: {num_no_updates}')

# Guardar los resultados en archivos JSON de salida
with open(output_part, 'w', encoding='utf-8') as output_file:
    json.dump(recent_updates, output_file, indent=4)

with open(output_part_not, 'w', encoding='utf-8') as output_file_not:
    json.dump(no_updates, output_file_not, indent=4)

print(f'Resultados de partes actualizadas guardados en {output_part}')
print(f'Resultados de partes sin cambios guardados en {output_part_not}')
