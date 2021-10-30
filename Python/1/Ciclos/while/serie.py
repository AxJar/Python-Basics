"""
Programa para crear series
Axel Jarquin
entrada: el numero que me de el usuario
salida: serie del numero hasta el 1000
proceso:sumo el num que me de el usuario en cada vuelta de ciclo
"""
print("Este programa imprime la serie del numero que me des")
num=int(input("Dame un numero para hacer la serie hasta 100 "))

serie=num
cont=1
while serie <= 100 and serie> 0:
    print(serie, end="\t")
    if cont% 5 == 0:
        print("\n")
    cont=cont + 1
    serie = serie+num