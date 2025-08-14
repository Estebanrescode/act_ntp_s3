frase = "programacion es divertida"
vocales = "a,e,i,o,u"
contadorVocales = 0

for letra in frase:
    if letra.lower() in vocales:
        contadorVocales += 1

        print(f"cantidad de vocales en la frase : {contadorVocales}")


