'''
Programa que recibe del usuario un número entero que representa la cantidad de números que va a ingresar.
El programa recibe esa cantidad de números enteros, los coloca en una lista y la desplegará a pantalla.
Posteriormente construye una nueva lista, con el cuadrado de cada uno de los elementos de la lista del usuario.
'''
def captura_lista():
    l = []
    cuantos = int(input())
    for i in range(cuantos):
        dato = int(input())
        l.append(dato)
    return l

def lista_cuadrado():
    l_c = []
    for elemento in lista:
        elemento = elemento * elemento
        l_c.append(elemento)
    return l_c

lista = captura_lista()
print(lista)
l_cuadrado = lista_cuadrado()
print(l_cuadrado)


