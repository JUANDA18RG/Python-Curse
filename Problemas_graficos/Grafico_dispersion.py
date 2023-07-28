import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos de entrada
df = pd.read_csv("Problemas_graficos\\dispersion.csv")

# se crea una grafica de barras
sns.scatterplot(x="tiempo", y="dinero", data=df)
# mostrando el grafico
plt.show()
