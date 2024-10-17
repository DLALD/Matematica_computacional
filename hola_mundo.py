# Contar el número de palabras de un texto usando un ciclo for, sin contar comas
print("===================================================================================")
print("Taller de repaso ejercicio 14 lección 5")
print("===================================================================================")
# Descripción del ejercicio
print("Leer una frase y determinar cuántas palabras tiene")
print("===================================================================================")

oracion = "Este es un ejemplo de una oración para contar palabras, sin contar comas."
palabras = oracion.replace(",", "").split()
count = 0

for palabra in palabras:
    count += 1

print(f'La oración tiene {count} palabras.')
print(palabras)
