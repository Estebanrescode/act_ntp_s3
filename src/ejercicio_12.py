# Utilizando un ciclo while, calcula el factorial de un número entero n introducido por el usuario y muestra el resultado.

n = int(input("Ingresa un número entero positivo: "))

# Validar que el número sea positivo o cero
n = int(input("Número: "))
f, i = 1, 1
while i <= n: f *= i; i += 1
print(f"Factorial: {f}" if n >= 0 else "No válido")
