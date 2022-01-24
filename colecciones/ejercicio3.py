# Crear un programa que almacene con dos opciones: 
# 1. Agregar personas: permite introducir nombres de personas de forma interactiva, 
# 2. Sorteo: devuelve el nombre de una persona al azar. 
# Opcional: Cargar nombre a partir de un archivo csv.

print("1. Agregar personas")
print("2. Sorteo")
print("3. Salir")

opcion = int(input())
lista = []
salir_bool = False
while opcion != 3:
    if opcion == 1:
        nombre = input("Introduce un nombre: ")
        lista.append(nombre)
    if opcion == 2 and len(lista) != 0:
        print("El ganador del  sorteo es: ",lista.pop())
         # pop eliminaria el elemento de la lista, si no se quisiese eliminar, se podría imoplementar
         # la librería random y con random.choice(lista) sacaría un elemento aleatorio de la lista.
         # Otra solución con la librería random sería generar un número aleatorio 
         # num_aleatorio = randint(0, len(lista)) y sacar el ganador del sorteo por el índice
         # print(lista[num_aleatorio]) 
    print("1. Agregar personas")
    print("2. Sorteo")
    print("3. Salir")
    opcion = int(input())

csv = open("nombre_ejercicio3.csv")
lista_csv = csv.readlines()
print(lista_csv)
csv.close()