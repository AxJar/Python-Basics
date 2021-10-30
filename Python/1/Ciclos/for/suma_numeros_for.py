'''
programa para practicar uso de for
'''
print("Este programa suma desde 1 hasta el numero que me des ")
num = int(input("Dame hasta que numero deseas la suma: "))
suma = 0
for i in range (num+1):
    suma = suma+i
    print(f"La suma de 1 hasta {num} es {suma}")