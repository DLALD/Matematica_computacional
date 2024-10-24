import pandas as pd
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.head())
# Filtrar las personas que sobrevivieron y que tenían más de 61 años
sobrevivientes_mayores_61 = df[(df['Survived'] == 1) & (df['Age'] >= 60)]


print(sobrevivientes_mayores_61.to_string(index=False))
#promedio de edad de personas fallecidas
fallecidos = df[df['Survived'] == 0]


edad_promedio_fallecidos = fallecidos['Age'].mean()

print(f"La edad promedio de las personas fallecidas es {edad_promedio_fallecidos:.2f} años.")

#menores de 10 años que sobrevivieron
menores_10_sobrevivientes = df[(df['Survived'] == 1) & (df['Age'] < 10)]

cantidad_menores_10_sobrevivientes = menores_10_sobrevivientes.shape[0]

print(f"La cantidad de pasajeros menores de 10 años que sobrevivieron es {cantidad_menores_10_sobrevivientes}.")

