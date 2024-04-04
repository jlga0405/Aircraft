def divide_archivo(input_file, output_prefix, items_per_file=1500):
    with open(input_file, 'r') as file:
        content = file.readlines()

    num_items = len(content)

    for i in range(0, num_items, items_per_file):
        start = i
        end = min(i + items_per_file, num_items)
        parte = content[start:end]

        output_file = f"{output_prefix}{i//items_per_file + 1:03d}.txt"
        with open(output_file, 'w') as file:
            file.writelines(parte)

if __name__ == "__main__":
    input_file = "data.txt"   # El archivo 'data.txt' está en la misma ubicación que este script
    output_prefix = "parte"  # Prefijo para los archivos de salida
    items_per_file = 1500     # Número de ítems por archivo

    divide_archivo(input_file, output_prefix, items_per_file)
