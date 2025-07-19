# Con un ciclo for, cuenta cuántas vocales (sin distinción de mayúsculas/minúsculas) hay en la frase frase = "programacion es divertida" y muestra el total.

frase = "programacion es divertida"
vocales = "a,e,i,o,u"
contadorVocales = 0

for letra in frase:
    if letra.lower() in vocales:
        contadorVocales += 1

        print(f"cantidad de vocales en la frase : {contadorVocales}")


