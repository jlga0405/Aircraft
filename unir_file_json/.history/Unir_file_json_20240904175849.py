import json
import pandas as pd

# Nombres de los archivos JSON de entrada
file_json2 = 'incorashop_02.json'
file_json3 = 'incorashop_03.json'
file_json1 = 'incorashop_01.json'
file_json4 = 'incorashop_04.json'
file_json5 = 'incorashop_05.json'
file_json6 = 'incorashop_06.json'
file_json7 = 'incorashop_07.json'
file_json8 = 'incorashop_08.json'

# Nombre del archivo JSON de salida
file_output = 'output_KLX_General.json'

# Nombre del archivo Excel de salida
excel_output = 'output_KLX_General.xlsx'

# Lista para almacenar todos los datos combinados
combined_data = []

# Lista con todos los archivos JSON de entrada
file_list = [file_json1, file_json2, file_json3, file_json4, file_json5, file_json6, file_json7, file_json8]

# Leer y combinar datos de cada archivo JSON
for file_name in file_list:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            combined_data.extend(data)
    except FileNotFoundError:
        print(f"El archivo {file_name} no fue encontrado y será omitido.")
    except json.JSONDecodeError:
        print(f"Error al leer el archivo {file_name}. Asegúrate de que esté correctamente formateado.")

# Escribir los datos combinados en el archivo JSON de salida
with open(file_output, 'w', encoding='utf-8') as output_file:
    json.dump(combined_data, output_file, ensure_ascii=False, indent=4)

print(f"Los datos han sido combinados y guardados en {file_output}")

# Convertir el archivo JSON a Excel
try:
    # Leer los datos del archivo JSON de salida
    with open(file_output, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # Convertir los datos a un DataFrame de Pandas
    df = pd.DataFrame(data)
    
    # Dividir los datos en múltiples hojas para evitar el límite de URLs
    chunk_size = 65000  # Ajusta según sea necesario
    with pd.ExcelWriter(excel_output, engine='xlsxwriter') as writer:
        for i in range(0, len(df), chunk_size):
            df_chunk = df.iloc[i:i+chunk_size]
            sheet_name = f'Sheet_{i//chunk_size + 1}'  # Nombre de la hoja basado en el número de chunk
            df_chunk.to_excel(writer, sheet_name=sheet_name, index=False)
    
    print(f"El archivo Excel ha sido generado como {excel_output}")
except Exception as e:
    print(f"Se produjo un error al convertir el archivo JSON a Excel: {e}")
