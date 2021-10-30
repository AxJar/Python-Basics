'''
De una lista de números definida. Determinar cuántos están entre -5 y 5 (sin incluirlos), cuántos menores o iguales a -5 y cuántos mayores o iguales a 5.
'''
lista = [1, 2, 3, -6]

menor = 0
entre = 0
mayor = 0
for elemento in lista:
    if elemento < -5:
        menor = menor + 1
    if elemento < 5:
        entre = entre + 1
    else:
        mayor = mayor + 1

print(menor)
print(entre)
print(mayor)
