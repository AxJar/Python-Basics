'''
Programa con funciones de listas
'''
def captura_lista():
    l = []                       #La lista debe estar inicializada en VACIÓ
    cuantos = int(input("Cuantos datos me vas a dar? "))
    for i in range(cuantos):     #Range para ir avanzando en el FOR
        dato = int(input("Dame un dato: "))
        l.append(dato)           #append AGREGA al final de la lista el dato
    return l

def imprime_lista(l):            #función para imprimir listas
    for elemento in l:
        print(f"{elemento}", end = " ")
    print()


# Programa Principal
print("Este programa manipula listas")
lista = captura_lista()
print(lista)
imprime_lista(lista)
