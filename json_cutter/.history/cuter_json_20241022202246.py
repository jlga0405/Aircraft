import json
import os

def split_json_file(file_path, chunk_size, output_base_name):
    with open(file_path, 'r') as file:
        data = json.load(file)

    total_chunks = len(data) // chunk_size + (1 if len(data) % chunk_size != 0 else 0)

    for i in range(total_chunks):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size

        chunk_data = data[start_idx:end_idx]
        chunk_file_name = f"{output_base_name}_{i + 1:02d}.json"  # Nombre de archivo basado en el nombre base y el contador

        with open(chunk_file_name, 'w') as chunk_file:
            json.dump(chunk_data, chunk_file, indent=2)

if __name__ == "__main__":
    json_file_path = "output_Lista_1878_07092024_wencor_49.json"
    output_base_name = "output_Lista_1878_07092024_wencor_49"  # Nombre base para los archivos de salida
    chunk_size = int(input("Ingrese el tamaño de cada parte: "))

    if not os.path.exists(json_file_path):
        print(f"El archivo {json_file_path} no existe.")
    else:
        split_json_file(json_file_path, chunk_size, output_base_name)
        print("El archivo se ha dividido en partes correctamente.")
