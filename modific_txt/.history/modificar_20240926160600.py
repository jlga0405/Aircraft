# Abre el archivo produc_code
with open('modific.txt', 'r') as infile:
    content = infile.read()

# Divide el contenido por comas,elimina los espacios en blanco
items = [item.strip() for item in content.split(',')]

# Define la cantidad máxima de elementos por línea (por ejemplo, 15)
max_elements_per_line = 1500

# Combina los elementos en líneas según el valor máximo
lines = [', '.join(items[i:i + max_elements_per_line]) for i in range(0, len(items), max_elements_per_line)]

# Combina las líneas en un bloque de texto
formatted_content = ',\n'.join(lines)


with open('outModific.txt', 'w') as outfile:
    outfile.write(formatted_content)
