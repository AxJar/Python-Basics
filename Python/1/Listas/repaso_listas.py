def captura_lista():
    cuantos = int(input("Cuantos datos me vas a dar = "))
    lis = []
    for i in range(cuantos):
        dato = input("Dame una palabra: ")
        lis.append(dato)
    return lis

def imprime_lista(lis):
    for palabra in lis:
        print(palabra)             # Imprime palabra por palabra

def imprime_indice(lis):
    for i in range(len(lis)):
        print(i)                   # Imprime indice

def imprime_lista_indice(lis):
    for i in range(len(lis)):
        print(lis[i])             # Imprime el contenido de cada posición en la lista

def cuenta_palabras(lis):
    cont = 0
    for palabra in lis:
        if palabra == "hola":
            cont = cont + 1
    print(f"La lista tiene {cont} palabras \"hola\"")

def cambia_palabras(lis):
    for i in range(len(lis)):
        if lis[i] == "hola":
            lis[i] = "adiós"
    print(lis)

# Programa principal
lista = captura_lista()
imprime_lista(lista)
imprime_indice(lista)
imprime_lista_indice(lista)
cuenta_palabras(lista)
cambia_palabras(lista)