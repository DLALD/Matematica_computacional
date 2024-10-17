
datos = [12, 25, 37, 44, 53, 61, 78, 89]


posicion = int(input("Ingrese la posición del elemento que desea ver (del 1 al 8): "))


posicion -= 1


if 0 <= posicion < len(datos):
    elemento = datos[posicion]
    print(f'El elemento en la posición {posicion + 1} es: {elemento}')
else:
    print("Posición no válida. Por favor, ingrese un número entre 1 y 7.")
