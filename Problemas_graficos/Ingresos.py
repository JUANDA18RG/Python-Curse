import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos de entrada
df = pd.read_csv("Problemas_graficos\\cofla_ingresos.csv")
# se crea una grafica de barras
sns.barplot(x="fuente", y="ingresos", data=df)
# total de ingresos
total = df["ingresos"].sum()
print(f'toral de ingresos: {total}')
# se muetra el grafico
plt.show()
