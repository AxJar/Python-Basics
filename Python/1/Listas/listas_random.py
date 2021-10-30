'''
Reto 1 :Genera una lista de 10 elementos con números random
Reto 2 :Encuentra cuál es el número máximo generado
Reto 3 :Encuentra cuál es el número mínimo
Reto 4 :Copia la primera lista a otra lista
Reto 5 :Ordena la segunda lista de mayor a menor
Reto 6 :De la lista ordenada, suma los elementos que se encuentran en las posiciones pares.
Reto 7 :De la lista ordenada suma todos los números impares.
'''
import random

def genera_lista_random(r):
    l_rand = []                           # Paso 1: Inicializar la lista a lista vacia
    for i in range(10):                   # Paso 2: Genero un for hasta 10
        dato = random.randint(1, r)       # Paso 3: Genero un numero random
        l_rand.append(dato)               # Paso 4: Appeneo dato a l_rand
    return l_rand

def imprime_lista(l):                     # función para imprimir listas
    for elemento in l:
        print(f"{elemento}", end = " ")
    print()

def suma_impares(l):
    suma = 0
    for elemento in l:                    # Elemento va tomando cada uno de los valores en l (que es la lista)
        if elemento % 2 != 0:             # Reviso si el elemento es impar
            suma = suma + elemento
    return suma

def  suma_posicion_par(l):
    suma = 0
    for i in range(len(l)):               # Necesito que i camine por los valores 0, 1, 2, 3
        if i % 2 == 0:                    # Si la posición es par: 0, 2, 4 se va a sumar el contenido
            suma = suma + l[i]            # de l[i] (no importa que el contenido NO sea par)
    return suma

# Programa principal
print("Este programa manipula una lista de numero random")
tope = int(input("Cual quieres que sea el tope de rango para los números random? "))
lista = genera_lista_random(tope)         # l_rand la voy a guardar en lista
imprime_lista(lista)
print(f"El numero máximo generado es {max(lista)}")
print(f"El numero mínimo generado es {min(lista)}")
lista2 = lista
lista2.sort(reverse = True)
print("La lista generada en forma descendente quedo asi:")
imprime_lista(lista2)
impares = suma_impares(lista2)
print(f"La suma de los números impares dentro de la lista es {impares}")
pares = suma_posicion_par(lista2)
print(f"La suma de los números en posición par dentro de la lista es {pares}")
