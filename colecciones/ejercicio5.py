# Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
# Crear una nueva lista con los nombres ordenados alfabéticamente e imprimirla por pantalla. 


lista = []
while len(lista) < 5:
    nombre = input("Ingresa nombres: \n")
    lista.append(nombre)
lista.sort()
print(lista)

# Opcional: Crea una función que ordene os nombres por su longitud para pasársela como parámetro al método Short.

def funcion_ejemplo(a,*lista):
    print(a)
    print(type(a))
    print(type(lista))
    print(lista)
    for elemento in lista:
        print(elemento)

funcion_ejemplo("Juan","Jaime","Maria","Andrés")