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

    # Eliminar duplicados
    df_sin_duplicados = eliminar_duplicados(df)

    # Obtener el tamaño del archivo .xlsx
    archivo_size = os.path.getsize(ruta_archivo_xlsx)

    # Mostrar una barra de progreso
    with tqdm(total=archivo_size, unit="B", unit_scale=True) as pbar:
        # Convertir el DataFrame a .csv
        df_sin_duplicados.to_csv(ruta_archivo_csv, index=False, chunksize=100000)

# Obtener la ruta de la carpeta donde está el archivo .py
ruta_carpeta_py = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta del archivo .xlsx
ruta_archivo_xlsx = os.path.join(ruta_carpeta_py, "data.xlsx")

# Ruta del archivo .csv donde se guardará el resultado
ruta_archivo_csv = os.path.join(ruta_carpeta_py, "output_data.csv")

# Convertir el archivo .xlsx a .csv
convertir_xlsx_a_csv(ruta_archivo_xlsx, ruta_archivo_csv)
