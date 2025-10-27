#leyendo un archivo csv
import pandas as pd
df = pd.read_csv("Facturacion.csv", sep=";")
print(df)
