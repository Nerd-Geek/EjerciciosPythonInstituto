# Crear un programa “Diccionario” que permita consultar definiciones, 
# agregar nuevas palabras con su definición o eliminar palabras. 

diccionario = {}
acabar = False
print("1. Agregar palabra y definición")
print("2. Consultar una definición")
print("3- Eliminar palabra")
print("4. Salir")
opcion = int(input("¿Qué deseas?\n"))
while opcion != 4:
    if opcion == 1:
        palabra = input("Introduce una palabra: \n")
        definicion = input("Introdcue su definición: \n")
        diccionario.setdefault(palabra,definicion)
    if opcion == 2:
        buscar = input("¿Qué palabra desea buscar?\n")
        encontrado = diccionario.get(buscar)
        print(encontrado)
    if opcion == 3:
        eliminar = input("¿Qué palabra deseas eliminar?\n")
        diccionario.pop(eliminar)
    print("1. Agregar palabra y definición")
    print("2. Consultar una definición")
    print("3- Eliminar palabra")
    print("4. Salir")
    opcion = int(input("¿Qué deseas?\n"))

# Opcional: Cargar diccionario a partir de un archivo csv.

csv = open("nombre_ejercicio4.csv")
diccionario_csv = csv.readlines()
print(diccionario_csv)