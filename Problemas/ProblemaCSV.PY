import pandas as pd
df = pd.read_csv("Problemas\\texto.csv")
# convertir a string
df['edad'] = df['edad'].astype(str)
# mostar el tipo de dato
print(type(df['edad'][0]))
# remplazando los valores de la columna nombre
df['nombre'].replace("juan", "ingeniero", inplace=True)
# imprimiendo la columna nombre
print(df["nombre"])
# esto es para eliminar los valores nulos y no los muestre
df = df.dropna()
print(df)
# elininado filas repetidas
df = df.drop_duplicates()
print(df)

# creando un csv con el dataframe resutanate
df.to_csv("Problemas\\texto2.csv", index=False)
