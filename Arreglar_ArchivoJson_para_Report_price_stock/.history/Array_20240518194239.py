import json

input_file_path = './quimicos_consumibles_lubricantes_completo_actual_areglada_17052024.json'
output_file_path = './reporte_price_stock_quimicos_consumibles_lubricantes_completo_actual_areglada_17052024.txt'

# Leer el archivo JSON
with open(input_file_path, 'r') as f:
    data = json.load(f)

# Generar la cadena larga
long_string = ""
for element in data:
    long_string += f'"{element["partNumber"]}",\n'
    print(f'"{element["partNumber"]}",')

# Escribir la cadena en el archivo de texto
with open(output_file_path, 'w') as f:
    f.write(long_string)
