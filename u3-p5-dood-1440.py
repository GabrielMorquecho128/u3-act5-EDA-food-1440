
import pandas as pd
import matplotlib.pyplot as plt

# marco morquecho NC 1440

# 1. leer el archivo csv comida pais india
df_food_india = pd.read_csv("indian_food.csv")
print("\n--- DATOS LEIDOS DESDE CSV, comida india 1440 ---")
print(df_food_india)
print("\n--- mostrar nombre comida + ingredientes 1440 ---")
recetas = df_food_india[["name", "ingredients"]]
print(recetas)
print("\n--- Tiempo de cocinado mostrar 10 registros con head 1440---")
nombre_y_hora = df_food_india[["name", "cook_time"]].head(10)
print(nombre_y_hora)
print("\n--- grafica comida (x) tiempo de cocinado (y) 1440---")
print("\n--- grafica comida (x) tecto a 30 grados ---")
nombre_y_hora.plot.bar(x="name", y="cook_time", rot=30)
plt.title("Comida tipica de india marco 1440")
plt.xlabel("Nombre del platillo")
plt.ylabel("Tiempo de cocinado")
plt.show()
plt.title("graficas de varias columnas 1440")
nombre_y_hora = df_food_india[['name', 'prep_time', 'cook_time']].head(10)
nombre_y_hora.plot.bar(x='name', rot=30)
plt.title("grafica de 2 columnas marco 1440")
plt.xlabel("Nombre del platillo")
plt.ylabel("Tiempo de cocinado prep y comida")
plt.show()
print("\n--- Graficas aoiladas una tras otra verticalmente 1440 ---")
nombre_y_hora.plot.bar(x='name', stacked=True,rot=30)
plt.title("grafica apiladas marco 1440")
plt.xlabel("Nombre del platillo")
plt.ylabel("Tiempo de cocinado prep y comida")
plt.show()