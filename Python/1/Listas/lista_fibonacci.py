""" Programa que lee la cantidad de n elementos que desea tener en la lista.
El programa valida que n sea mayor o igual que 0, de lo contrario lo vuelve a solicitar. Como resultado, 
se despliega la lista con los primeros n elementos de la serie de Fibonacci.
"""
"""
Entrada
Un número entero positivo que corresponde al número de términos de la serie de Fibonacci que queremos en la lista. Si el dato recibido es menor que 0, se debe volver a solicitar.

Salidas
La lista con el número de términos de la serie de Fibonacci solicitados.

Ejemplos de ejecución del programa
 >  >  > 5
[0, 1, 1, 2, 3]

 >  >  > 9
[0, 1, 1, 2, 3, 5, 8, 13, 21]

 >  >  > 0
[ ]
"""
while True:
    n = int(input())
    if n >= 0:
        break

l = []
if n == 0:
    print(l)
else:
    ult = 0
    act = 1
    for i in range(n):
        l.append(ult)
        suma = ult + act
        ult = act
        act = suma
    print(l)
