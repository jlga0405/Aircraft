import pandas as pd

def csv_to_xlsx(csv_file, xlsx_file):
    try:
        # Lee el archivo CSV
        df = pd.read_csv(csv_file)
        
        # Escribe el DataFrame en un archivo XLSX
        df.to_excel(xlsx_file, index=False)
        
        print(f"¡El archivo {csv_file} ha sido convertido a {xlsx_file} exitosamente!")
    except Exception as e:
        print("Ha ocurrido un error:", e)

if __name__ == "__main__":
    # Nombre del archivo CSV de entrada
    csv_file = "volutionPriceOutput-Lista_Nicrocraft.csv"
    # Nombre del archivo XLSX de salida
    xlsx_file = "volutionPriceOutput-Lista_Nicrocraft.xlsx"
    
    # Llama a la función para convertir CSV a XLSX
    csv_to_xlsx(csv_file, xlsx_file)
