# Mediante un ciclo while, solicita al usuario que escriba palabras. El proceso termina cuando el usuario escriba la palabra “fin”. Al final, muestra cuántas palabras se leyeron (sin contar “fin”).

contador = 0

while True:
    palabra = input("Escribe 'fin' para terminar ")
    if palabra.lower() == "fin":
        break
    contador += 1

print(f"Se leyeron {contador} palabras.")
