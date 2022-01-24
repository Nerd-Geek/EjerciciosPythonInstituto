# Crear un programa que almacene nombres de personas, tras introducir un nombre 
# nuevo mostrará un conteo de los nombres que tienen 5 o más caracteres y 
# preguntará si desea introducir un nuevo nombre o salir del programa. 
# Opcional: Cargar palabras a partir de un archivo txt.

salir = False
lista = []
nombre = ""
while salir == False:
    nombre = input("Escriba un nombre: ")
    lista.append(nombre)
    conteo = 0
    for i in range(0,len(lista)):
        if len(lista[i])>= 5:
            conteo+=1
    print(conteo)
    print("¿Desea introducir un nuevo nombre?")
    opcion = input()
    if opcion == "No":
        salir = True

f = open("nombres.txt")
fichero = f.readlines()
nueva_lista = fichero
conteo_nuevo = 0
for i in range(0, len(nueva_lista)):
    if len(nueva_lista[i]) >= 5:
        conteo_nuevo += 1
f.close()
print(conteo_nuevo)