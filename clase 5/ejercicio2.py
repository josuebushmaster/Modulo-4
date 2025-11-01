import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from pathlib import Path

# Cargar datos — usar rutas relativas al script para evitar FileNotFoundError cuando
# el script se ejecuta desde otra carpeta (CWD distinto).
base = Path(__file__).parent
df_train = pd.read_excel(str(base / "DatosAbandonoClientesTrain.xlsx"))
df_predict = pd.read_excel(str(base / "DatosAbandonoClientesPredict.xlsx"))


#Sacar copias de DataFrame para procesamiento
df_train_copia = df_train.copy()
df_predict_copia = df_predict.copy()

#Tratando las variables categorias
categorias_cols = ["customerGender","region"]

#Codificacion de variables
encoder = {}
for col in categorias_cols:
    enc = LabelEncoder()
    df_train_copia[col] = enc.fit_transform(df_train_copia[col])
    df_predict_copia[col] = enc.transform(df_predict_copia[col])
    encoder[col] = enc

#Convertir la columna predictora (lostToCompetitor) a numerica
df_train_copia["lostToCompetitor"] = df_train_copia["lostToCompetitor"].map({"no" : 0, "yes" : 1})

#Definir variables predictoras y objetivo
X_train = df_train_copia.drop(columns=["lostToCompetitor"])
y_train = df_train_copia["lostToCompetitor"]

#Entrenar el algoritmo Regresion logistica
modelo1 = LogisticRegression(max_iter=1000)
modelo1.fit(X_train, y_train)

#Prediccion
predicciones = modelo1.predict(df_predict_copia)

df_result = df_predict.copy()
df_result["Prediccion"] = predicciones

print(df_result)


# Exportar el DataFrame de resultados a un archivo Excel
output_file = str(base / "Resultados_Prediccion_clientes.xlsx") # Nombre del archivo de salida (en la misma carpeta que el script)
df_result.to_excel(output_file, index=False) # Guardar sin el índice
print(f"Resultados exportados a: {output_file}") # Confirmacion de exportacion



