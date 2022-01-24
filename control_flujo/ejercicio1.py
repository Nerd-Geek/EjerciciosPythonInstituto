# Programa que dibuje con asteriscos un triángulo rectángulo isósceles de N 
# asteriscos de alto. Opcional: pintar triangulo rectángulo escaleno.


n = int(input("Introduce el nº de asteríscos"))

for i in range(1,n):
    print(i*'*')
