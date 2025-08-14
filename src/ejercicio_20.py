mayor = -1 

while True:
    edad = int(input("Ingresa una edad (-1 para terminar): "))
    if edad == -1:
        break
    if edad > mayor:
        mayor = edad

print("La edad mayor ingresada fue:", mayor)
