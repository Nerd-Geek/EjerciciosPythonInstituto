# Solicitar una oración por teclado y realizar las siguientes operaciones sobre ella:
    # Mostrar longitud de la cadena.
    # Mostrar espacios en blanco se ingresaron.
    # Mostrar toda la oración en letras mayúsculas.
    # Duplicar el contenido de la cadena.
    # Dividir la cadena en una lista de palabras y recorrerla mostrándola y numerando cada palabra.

oracion = str(input("Introduce una oración: "))
print("La longitud de la oración es:",len(oracion))
print("La oración tiene",oracion.count(" "),"espacios")
print("Mostrar toda la oración en letras mayúsculas.")
print(oracion.upper())
print("Duplicar el contenido de la cadena.")
print(2*oracion)
print("Dividir la cadena en una lista de palabras y recorrerla mostrándola y numerando cada palabra.")
nueva_oracion = oracion.split()
for i in range(0,len(nueva_oracion)):
    print((i+1),nueva_oracion[i])