'''
De una lista definida por el usuario, modifica sus números por el doble de su valor.
'''
def captura_lista():
    l = []
    cuantos = int(input())
    for i in range(cuantos):
        dato = int(input())
        l.append(dato)
    return l

def lis_doble_valor():
    l_d = []
    for elemento in lista:
        elemento = elemento * 2
        l_d.append(elemento)
    return l_d

lista = captura_lista()
lista_doble = lis_doble_valor()
print(lista_doble)
