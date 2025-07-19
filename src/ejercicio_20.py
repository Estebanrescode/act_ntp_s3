# Utilizando un ciclo while, solicita al usuario que ingrese edades una a una. El proceso termina cuando se introduzca -1. Al final, muestra la edad mayor que se haya ingresado.

mayor = -1 

while True:
    edad = int(input("Ingresa una edad (-1 para terminar): "))
    if edad == -1:
        break
    if edad > mayor:
        mayor = edad

print("La edad mayor ingresada fue:", mayor)
