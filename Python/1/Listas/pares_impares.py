'''
Programa que determina el total de valores pares e impares de una lista de números enteros que recibe en su entrada. Los valores los captura el usuario
uno por uno, se van almacenando en una lista y posteriormente se analizará la lista para determinar cuantos valores pares e impares posee. Consideramos al 0 como par.
'''
def cap_numeros():
    l = []
    datos = ''
    while datos != "*":
            datos = input()
            if datos == "*":
                break
            else:
                l.append(datos)
    return l

def impares(l):
    cont = 0
    for datos in l:
        if int(datos) % 2 != 0:
            cont = cont+1
    return cont

def pares(l):
    cont2 = 0
    for datos in l:
        if int(datos) % 2 == 0:
            cont2 = cont2 + 1
    return cont2

lista = cap_numeros()
lista_2 = lista
contador_pares = pares(lista_2)
print(f"PARES = {contador_pares}")
contador_impares = impares(lista_2)
print(f"IMPARES = {contador_impares}")

