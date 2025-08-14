contador = 0

while True:
    palabra = input("Escribe 'fin' para terminar ")
    if palabra.lower() == "fin":
        break
    contador += 1

print(f"Se leyeron {contador} palabras.")
