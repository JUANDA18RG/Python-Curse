import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos de entrada
df = pd.read_csv("Problemas_graficos\\bigotes.csv")
sns.boxplot(x="categoria", y="valor", data=df)

# mostrando el grafico
plt.show()
