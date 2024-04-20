import os
import csv

def split_csv_file(file_path, chunk_size, output_base_name):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = list(reader)

    total_chunks = len(data) // chunk_size + (1 if len(data) % chunk_size != 0 else 0)

    for i in range(total_chunks):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size

        chunk_data = [headers] + data[start_idx:end_idx]
        chunk_file_name = f"{output_base_name}_{i + 1:02d}.csv"

        with open(chunk_file_name, 'w', newline='') as chunk_file:
            writer = csv.writer(chunk_file)
            writer.writerows(chunk_data)

if __name__ == "__main__":
    csv_file_path = "volutionPriceOutput-List_CP30_15042024.csv"
    output_base_name = "volutionPriceOutput-List_CP30_15042024"
    chunk_size = int(input("Ingrese el tamaño de cada parte: "))

    if not os.path.exists(csv_file_path):
        print(f"El archivo {csv_file_path} no existe.")
    else:
        split_csv_file(csv_file_path, chunk_size, output_base_name)
        print("El archivo se ha dividido en partes correctamente.")
