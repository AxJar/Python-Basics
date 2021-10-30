'''
Programa para practicar for con impresion de triangulos de asteriscos
'''
print("Este programa dibuja un triangulo con asteriscos")
num = int(input("De cuantos asteriscos quieres la base del triangulo? "))
for i in range(1, num+1):
    print("*"*i)

for i in range(num, 0-1, -1):
    print("*"*i)