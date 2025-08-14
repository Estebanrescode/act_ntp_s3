total = 0
while True:
    n = input("Ingresa un numero: ")
    if n == "0":
        break
    total += int(n)
print("Total:", total)