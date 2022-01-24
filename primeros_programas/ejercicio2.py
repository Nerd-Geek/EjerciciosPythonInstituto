# Haz un programa que adivine la talla de pie y la edad del usuario que lo ejecute.
# Se basa en un sencillo truco matemático. El programa debe pedir al usuario que 
# realice las siguientes operaciones (las operaciones la tiene que realizar el de 
# cabeza, no el programa):

# Pensar, escribir o apuntar su talla de zapato.
# Multiplicar ese número por 5.
# Sumarle 50.
# Multiplicarlo por 20.
# Sumarle 1021.
# Restarle el año de nacimiento.

from time import sleep

print("Piensa en tu talla de zapato.")
sleep(3.0)
print("Multiplicar ese número por 5.")
sleep(3.0)
print("Sumarle 50.")
sleep(3.0)
print("Multiplicarlo por 20.")
sleep(3.0)
print("Sumarle 1021.")
sleep(3.0)
print("Restarle el año de nacimiento.")
sleep(3.0)
respuesta = input("Introduce tu resultado: ")
print("Tu talla es:",respuesta[0]+""+respuesta[1],",tu edad es:",respuesta[2]+""+respuesta[3])

#talla = int(input("Introduce la talla: "))
#dato = int(input("Multiplicar ese número por 5: "))
#resultado = talla * dato
#dato = int(input("Sumarle 50: "))
#resultado += dato
#dato = int(input("Multiplicarlo por 20: "))
#resultado *=  dato 
#dato = int(input("Sumarle 1021: "))
#resultado += dato
#dato = int(input("Restarle el año de nacimiento: "))
#resultado -= dato
#resultado_final = str(resultado)

#print("Tu talla es:",resultado_final[0]+""+resultado_final[1],", tu edad es:",resultado_final[2]+""+resultado_final[3])