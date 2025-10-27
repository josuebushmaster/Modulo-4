import pandas as pd 

df = pd.DataFrame({
    "Nombres" : ["Ana", "Luis", "Josue", "Kenia"],
    "Edad" : [23, 34, 45, 25],
    "Genero" : ["F", "M", "M", "F"]
})
print(df)
print(type(df))
print("-------------------------")
#Obteniendo una serie del DataFrame
s1=df["Nombres"]
print(s1)

