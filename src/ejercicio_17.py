# Con un ciclo for, solicita al usuario que ingrese un número entero positivo y calcula la suma de sus dígitos, mostrando el resultado final.
numero = input("ingresa un numero entero positivo")
suma_digitos = sum(int(digito)for digito in numero)
print(f"la suma de los digitos es :{suma_digitos}")