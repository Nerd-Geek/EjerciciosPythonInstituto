# Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.

lista = [5,6,7,8,9]

for i in range(0,len(lista)):
    numero = lista[i]
    if numero >= 7:
        print(numero)