import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos de entrada
df = pd.read_csv("Problemas_graficos\\pedos.csv")
sns.lineplot(x="fecha", y="pedos", data=df)


# marcar el punto mas alto de la grafica con un punto rojo
plt.plot("12-20", 9, "o")
plt.text("12-20", 9, "Maximo", fontsize=10, color="red")
plt.plot("01-08", 9, "ro")
plt.text("01-08", 9, "Maximo", fontsize=10, color="red")

# mostrando el grafico
plt.show()
