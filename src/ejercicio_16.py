# Utilizando un ciclo while, simula un reloj digital que muestre cada segundo desde 00:00 hasta 00:59 en formato MM:SS, cada valor en una línea.

segundos = 0
while segundos <60:
    print(f"00:{str(segundos).zfill(2)}")
    segundos +=1