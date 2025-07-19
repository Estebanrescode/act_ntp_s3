# Mediante un ciclo while, implementa un juego de adivinanza: el programa genera un número aleatorio del 1 al 10 y solicita al usuario que lo adivine. El proceso se repite hasta que el usuario acierte. Muestra un mensaje de felicitación al final.

import random

numero_aleatorio = random.randint(1 , 10)
while True:
    intengo = int(input("adivina el numero del 1 al 10:"))
    if intengo == numero_aleatorio:
        print("Felicitaciones")
        break
    else:
        print("intenta de nuevo")
   