import os
import pandas as pd
from tqdm import tqdm

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

  # Obtener el tamaño del archivo .xlsx
  archivo_size = os.path.getsize(ruta_archivo_xlsx)

  # Mostrar una barra de progreso
  with tqdm(total=archivo_size, unit="B", unit_scale=True) as pbar:
    # Convertir el DataFrame a .csv
    df.to_csv(ruta_archivo_csv, index=False, chunksize=100000, on_write=pbar.update)


# Obtener la ruta del archivo .py actual
ruta_archivo_py = os.path.abspath(__file__)

# Obtener la ruta de la carpeta donde está el archivo .py
ruta_carpeta_py = os.path.dirname(ruta_archivo_py)

# Construir la ruta del archivo .xlsx
ruta_archivo_xlsx = os.path.join(ruta_carpeta_py, "archivo.xlsx")

# Ruta del archivo .csv donde se guardará el resultado
ruta_archivo_csv = os.path.join(ruta_carpeta_py, "archivo.csv")

# Convertir el archivo .xlsx a .csv
convertir_xlsx_a_csv(ruta_archivo_xlsx, ruta_archivo_csv)
