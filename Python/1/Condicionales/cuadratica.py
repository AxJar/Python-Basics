""" Realiza un programa para calcular los valores de la ecuación cuadrática ax^2+bx+c usando la fórmula cuadrática.
El programa lee tres valores enteros a, b y c, y encuentra los valores de x, considerando las siguientes restricciones:

- Si a = 0 y b = 0 se debe desplegar el mensaje "No tiene solución”
- Si a = 0 y b != 0 se debe despejar el valor de x = –c/b y mostrar este valor.
- Si a != 0 y b != 0 se debe calcular el discriminante.
* Si el valor del discriminante es negativo debe mostrar el mensaje "Raices complejas"
* Si el valor del discriminante es positivo debe calcular y mostrar los dos valores de x, una en cada renglón
* En caso de que el discriminante sea cero se debe mostrar sólo un valor de x = -b/(2a) """

from math import *
a = int(input())
b = int(input())
c = int(input())
dis = (b**2)-4*(a)*(c)
if a == 0 and b == 0:
    print("No tiene solucion")
elif a == 0 and b != 0:
    print(-c/b)
elif a != 0 and b != 0:
    if dis < 0:
        print("Raices complejas")
    elif dis > 0:
        print(((-b)+sqrt((b**2)-(4)*(a)*(c)))/2*a)
        print(((-b)-sqrt((b**2)-(4)*(a)*(c)))/2*a)
    else:
        print(-b/(2*a))