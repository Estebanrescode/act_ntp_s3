# Usando un ciclo while, calcula y muestra los cuadrados de los números del 1 al 20 (1², 2², …, 20²), cada resultado en una línea.

numero = 1

while numero <= 20:
    cuadrado = numero ** 2
    print(f"{numero}² = {cuadrado}")
    numero += 1


