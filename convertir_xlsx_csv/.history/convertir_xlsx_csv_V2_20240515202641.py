import os
import pandas as pd
from tqdm import tqdm

def eliminar_duplicados(df):
    """
    Elimina los duplicados del DataFrame.

    Args:
        df: DataFrame de Pandas.

    Returns:
        DataFrame sin duplicados.
    """
    return df.drop_duplicates()


def convertir_xlsx_a_csv(ruta_archivo_xlsx, ruta_archivo_csv):
    """
    Convierte un archivo .xlsx a .csv, mostrando una barra de progreso.

    Args:
        ruta_archivo_xlsx: Ruta al archivo .xlsx que se desea convertir.
        ruta_archivo_csv: Ruta al archivo .csv donde se guardará el resultado.

    Returns:
        None
    """

    # Leer el archivo .xlsx
    df = pd.read_excel(ruta_archivo_xlsx)

    # Obtener la cantidad de duplicados
    cantidad_duplicados = len(df) - len(eliminar_duplicados(df))

    if cantidad_duplicados > 0:
        print(f"Se eliminaron {cantidad_duplicados} duplicados.")

        # Guardar los duplicados en un archivo de texto
        duplicados_file = os.path.join(ruta_carpeta_py, "duplicados.txt")
        df[df.duplicated()].to_csv(duplicados_file, index=False, sep='\t')

        print(f"Los duplicados se han guardado en {duplicados_file}")

    else:
        print("No se encontraron duplicados.")

    # Eliminar duplicados
    df_sin_duplicados = eliminar_duplicados(df)

    # Obtener el tamaño del archivo .xlsx
    archivo_size = os.path.getsize(ruta_archivo_xlsx)

    # Mostrar una barra de progreso
    with tqdm(total=archivo_size, unit="B", unit_scale=True) as pbar:
        # Convertir el DataFrame a .csv
        df_sin_duplicados.to_csv(ruta_archivo_csv, index=False, chunksize=100000)


# //////////Nombre del archivo de entrada .xlsx///////////
archivo_in = "volutionPriceOutput-Lista_SP_SS_13.xlsx"

# //////////Nombre del archivo de salida .csv//////////
archivo_output = "volutionPriceOutput-Lista_SP_SS_13.csv"

# Obtener la ruta de la carpeta donde está el archivo .py
ruta_carpeta_py = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta del archivo .xlsx
ruta_archivo_xlsx = os.path.join(ruta_carpeta_py, archivo_in)

# Ruta del archivo .csv donde se guardará el resultado
ruta_archivo_csv = os.path.join(ruta_carpeta_py, archivo_output)

# Convertir el archivo .xlsx a .csv
convertir_xlsx_a_csv(ruta_archivo_xlsx, ruta_archivo_csv)
