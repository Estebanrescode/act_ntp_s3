n = int(input("Ingresa un número entero positivo: "))
n = int(input("Número: "))
f, i = 1, 1
while i <= n: f *= i; i += 1
print(f"Factorial: {f}" if n >= 0 else "No válido")
