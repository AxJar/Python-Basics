'''
Programa que permite realizar la suma elemento a elemento de dos listas de números enteros y con la misma cantidad de elementos.
'''
elementos = int(input())
l1 = []
l2 = []
l3 = []

if elementos > 0:
    for i in range(elementos):
        datos = int(input())
        l1.append(datos)
    for i in range(elementos):
        datos = int(input())
        l2.append(datos)
    for i in range(elementos):
        l3.append(l1[i])
        l3[i] = l3[i] + l2[i]
    print(l3)
else:
    print("Error")

