import json

input_file_path = './LISTA_GRAL_AVIALL_29072024_CORRER.json'
output_file_path = './LISTA_GRAL_AVIALL_29072024_CORRER.txt'

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
