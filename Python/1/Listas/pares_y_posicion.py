'''
Programa que lee la cantidad de elementos que vas a ingresar de la lista, posteriormente cada uno de los elementos de la lista que son números enteros.
El programa después revisa la lista y para cada uno de los valores pares que encuentre muestra un mensaje que contenga la posición y el valor del numero par.
'''
'''
Entrada
Un número entero que representa la cantidad de valores que tiene la lista
Cada uno de los valores de la lista

Salida
Un mensaje para cada uno de los valores pares encontrados en la lista. El mensaje debe tener el formato:
pos XX, valor XX <  -- - Observa que va la palabra pos seguida de un número, después una coma, luego la palabra valor y luego otro número

Ejemplo de ejecución del programa:
 >  >  > 5
 >  >  > 1
 >  >  > 2
 >  >  > 3
 >  >  > 4
 >  >  > 5
pos 1, valor 2
pos 3, valor 4
'''
def lista_gen(n):
    lista = []
    for i in range(n):
        elem = int(input())
        lista.append(elem)
    return lista

def posiciones(lista, n):
    posiciones = []
    for i in range(n):
        if lista[i] % 2 == 0:
            posiciones.append(i)
    return posiciones

n = int(input())
lista = lista_gen(n)
posiciones = posiciones(lista, n)

for i in posiciones:
    print(f"pos {i}, valor {lista[i]}")