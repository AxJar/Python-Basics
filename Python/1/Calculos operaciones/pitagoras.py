'''
Este programa calcula la hipotenusa
AUTOR:Axel Jarquin Morga
ENTRADAS:cateto_a , cateto_b
PROCESO:Solicito los 2 catetos y los  guardo en su variable correspondiente
        Saco la raiz de la suma de cada cateto al cuadrado.
        Imprimo el resultado
SALIDAS:hipotenusa
'''
from math import *
print("Este programa calcula la hipotenusa, ingresa los catetos de tu triangulo")
cateto1 = float(input("Ingrese el primer cateto "))
cateto2 = float(input("Ingrese el segundo cateto "))
hipotenusa = pow(cateto1, 2)+pow(cateto2, 2)#pow eleva al numero que se le de
hipotenusa = sqrt(hipotenusa)
print("La hipotenusa es ", hipotenusa)