# Programa que adivine el numero en el que está pensando (entre 0 y 100) 
# el usuario por tanteo (preguntando sucesivamente si es mayor o menor 
# que un número aleatorio de partida)

import random

intentos = 0
adivinar = int()
num = random.randint(0,100)

adivinar = int(input("Intenta adivinar el número: "))
while adivinar != num:
    intentos += 1
    if adivinar < num:
        print("El número es mayor")
    if adivinar > num:
        print("El número es menor")
    if adivinar == num:
        break
    adivinar = int(input("Intenta adivinar el número: "))

print("Felicidades, adivinaste. El número era:", num)
print("Su número de intentos ha sido:",intentos)