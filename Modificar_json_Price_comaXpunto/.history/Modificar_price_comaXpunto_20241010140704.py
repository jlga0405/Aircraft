import json

# Lee el archivo JSON
with open('Act_Lonseal_precio_26032024.json', 'r') as f:
    data = json.load(f)

# Itera sobre cada objeto y modifica el valor de productprice
for product in data:
    # Convierte el valor de productprice a una cadena y luego realiza el reemplazo
    product['productweight'] = str(product['productweight']).replace(',', '.')

# Guarda el JSON modificado en un nuevo archivo
with open('archivo_modificado.json', 'w') as f:
    json.dump(data, f, indent=2)

print("El archivo modificado ha sido guardado correctamente como 'archivo_modificado.json'.")
