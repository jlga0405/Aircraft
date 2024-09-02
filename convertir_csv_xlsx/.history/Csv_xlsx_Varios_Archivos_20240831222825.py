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
    file_1 = "archivo1.csv"
    file_2 = "archivo2.csv"
    file_3 = "archivo3.csv"
    
    # Lista de archivos a procesar
    files = [file_1, file_2, file_3]
    
    # Itera sobre cada archivo y lo convierte si no está en blanco
    for file in files:
        if file:
            csv_to_xlsx(file)
