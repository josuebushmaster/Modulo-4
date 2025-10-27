#leyendo un archivo csv
from pathlib import Path # Manejo de rutas de archivos
import pandas as pd
base = Path(__file__).parent
df = pd.read_csv(base / "Facturacion.csv", sep=";")
print(df)
