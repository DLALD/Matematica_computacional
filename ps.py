import pandas as pd

# Crear un DataFrame
data = {
    'Nombre': ['Ana', 'Luis', 'María', 'Juan'],
    'Edad': [23, 35, 35, 40],
    'Nota': [3.5, 5.0, 4.5, 4.1]
}

df = pd.DataFrame(data)


# Calcular el promedio de la edad
promedio_edad = df['Edad'].mean()
print(f'El promedio de edad es: {promedio_edad}')

# Calcular el promedio de las notas
promedio_nota = df['Nota'].mean()
print(f'El promedio de las notas es: {promedio_nota}')

# Clasificar las notas
def clasificacion(nota):
    if nota >= 4.5:
        return 'Sobresaliente'
    elif nota >= 4.0:
        return 'Notable'
    elif nota >= 3.0:
        return 'Bien'
    elif nota >= 2.0:
        return 'Suficiente'
    else:
        return 'Insuficiente'

df['Clasificación'] = df['Nota'].apply(clasificacion)
print(df)
