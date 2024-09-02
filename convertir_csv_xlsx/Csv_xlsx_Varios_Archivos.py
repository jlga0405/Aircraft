import pandas as pd

def csv_to_xlsx(csv_file):
    try:
        # Genera el nombre del archivo XLSX basado en el nombre del archivo CSV
        xlsx_file = csv_file.replace(".csv", ".xlsx")
        
        # Lee el archivo CSV
        df = pd.read_csv(csv_file)
        
        # Escribe el DataFrame en un archivo XLSX
        df.to_excel(xlsx_file, index=False)
        
        print(f"¡El archivo {csv_file} ha sido convertido a {xlsx_file} exitosamente!")
    except Exception as e:
        print(f"Ha ocurrido un error al convertir {csv_file}:", e)

if __name__ == "__main__":
    # Variables con los nombres de los archivos CSV de entrada
    file_1 = "asap-list-v2-2024-09-01-not-found.csv"
    file_2 = "asap-list-v2-2024-09-01-out-of-range.csv"
    file_3 = "List_QLC_31082024.csv"
    
    # Lista de archivos a procesar
    files = [file_1, file_2, file_3]
    
    # Itera sobre cada archivo y lo convierte si no está en blanco
    for file in files:
        if file:
            csv_to_xlsx(file)
