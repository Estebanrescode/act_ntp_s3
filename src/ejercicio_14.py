import random

numero_aleatorio = random.randint(1 , 10)
while True:
    intengo = int(input("adivina el numero del 1 al 10:"))
    if intengo == numero_aleatorio:
        print("Felicitaciones")
        break
    else:
        print("intenta de nuevo")
   