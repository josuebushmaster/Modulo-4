import os # Para manejo de rutas de archivos
from pathlib import Path # Manejo de rutas de archivos
import pandas as pd # Manipulacion de datos
import csv
from sklearn.linear_model import LogisticRegression # Modelo de regresion logistica
from sklearn.preprocessing import LabelEncoder # Codificacion de variables categoricas

def read_table(path, show_type=False): # Funcion para leer CSV o Excel segun la extension
    """Lee un archivo CSV o Excel y devuelve (df, file_type, sep).

    sep será el separador detectado para CSV (',' o ';'), o None para Excel.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {path}")
    ext = path.suffix.lower()
    sep = None
    if ext == ".csv":
        # Detectar delimitador (',' o ';') usando csv.Sniffer
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            sample = f.read(4096)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=[',', ';'])
            sep = dialect.delimiter
        except Exception:
            # fallback: usar coma
            sep = ','
        df = pd.read_csv(path, sep=sep)
        file_type = 'CSV'
    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(path)
        file_type = 'Excel'
    else:
        raise ValueError("Formato no soportado. Usa .csv, .xls o .xlsx")

    if show_type:
        if sep:
            print(f"Archivo cargado: {path} (tipo: {file_type}, sep='{sep}')")
        else:
            print(f"Archivo cargado: {path} (tipo: {file_type})")

    return df, file_type, sep

# Rutas de entrada (usar rutas relativas al script para evitar FileNotFoundError)
base = Path(__file__).parent
train_file = base / "TitanicTraining.xlsx"
predict_file = base / "TitanicPredecir.xlsx"

# Cargar datos (detecta csv o excel) y mostrar tipo en consola
df_train, type_train, sep_train = read_table(train_file, show_type=True)
df_predict, type_predict, sep_predict = read_table(predict_file, show_type=True)

#Sacar copias de DataFrame para procesamiento
df_train_copia = df_train.copy()
df_predict_copia = df_predict.copy()

#Tratando las variables categorias
categorias_cols = ["Passenger Class", "Sex"]

#Codificacion de variables
encoder = {}
for col in categorias_cols:
    enc = LabelEncoder()
    df_train_copia[col] = enc.fit_transform(df_train_copia[col])
    df_predict_copia[col] = enc.transform(df_predict_copia[col])
    encoder[col] = enc

#Convertir la columna predictora (Survived) a numerica
df_train_copia["Survived"] = df_train_copia["Survived"].map({"No" : 0, "Yes" : 1})

#Definir variables predictoras y objetivo
X_train = df_train_copia.drop(columns=["Survived"])
y_train = df_train_copia["Survived"]

#Entrenar el algoritmo Regresion logistica
modelo1 = LogisticRegression(max_iter=1000)
modelo1.fit(X_train, y_train)

#Prediccion
predicciones = modelo1.predict(df_predict_copia)

df_result = df_predict.copy()
df_result["Prediccion"] = predicciones

print(df_result)

# Exportar el DataFrame de resultados a un archivo (extensión determina formato)
output_file = base / "Resultados_Prediccion.xlsx"  # cambia a "Resultados_Prediccion.csv" para CSV
if Path(output_file).suffix.lower() == ".csv":
    # si detectamos un separador en el archivo de entrada de predicción, usar el mismo
    sep_out = sep_predict if 'sep_predict' in globals() and sep_predict is not None else ','
    df_result.to_csv(output_file, index=False, sep=sep_out)
else:
    df_result.to_excel(output_file, index=False)
print(f"Resultados exportados a: {output_file}")