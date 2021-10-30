'''
Programa para practicar for y for anidado
'''
print("Este programa imprime la tabla de multiplicar del numero que me des ")
num = int(input("De que numero quieres la tabla de multiplicar? "))
for n in range(1, 6): #n = 1 2 3 4 5
    for i in range(1, 6): #Depende de cuantas vueltas quiero que de el ciclo
        print(f"{n} x {i} = {n*i}", end = "\t")
    print()
