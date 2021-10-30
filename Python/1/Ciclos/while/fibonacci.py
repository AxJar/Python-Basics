""" La secuencia de Fibonacci es una serie de números relacionados entre sí.
Usualmente la serie comienza con los números 0 y 1, y todo número sucesivo se calcula como la suma de los dos números anteriores.
Así que los primeros 11 elementos de la serie son:

0 1 1 2 3 5 8 13 21 34 55

Debes escribir un programa que contenga una función llamada fibonacci_index.
Esta función debe recibir como parámetro el indice (o posición) que quieres conocer dentro de la serie de Fibonacci.
La función debe regresar el número de Fibonacci en ese indice. Tu programa debe solamente imprimir el valor devuelto por la función. """

def fibonacci_index(indice):
    if indice == 1:
        fibo = 0
    elif indice == 2:
        fibo = 1
    else:
        ant = 0
        sig = 1
        cont = 2
        while cont < indice:
            fibo = ant+sig
            ant = sig
            sig = fibo
            cont = cont+1
    return fibo

posicion = int(input())
res = fibonacci_index(posicion)
print(res)

