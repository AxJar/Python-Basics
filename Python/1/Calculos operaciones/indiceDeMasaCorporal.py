'''Este programa calcula el indice de masa corporal de una persona, 
con los datos de peso y estatura que nos proporcione el usuario
AUTOR: Axel Jarquin Morga
Entradas: peso, estatura
PROCESO: Pido su estatura en metros, y la guardo en la variable
estatura.
Pido su peso en kilogramos y lo guardo en la variable peso.
Divido peso entre estatura al cuadrado y el resultado obtenido seria
el indice de masa corporal
SALIDAS:MasaCorporal
'''
print("Este programa calcula el indice de masa corporal , con tu peso y estatura")
peso = float(input("Dame tu peso en kilogramos "))
estatura = float(input("Dame tu estatura en metros "))
imc = peso/estatura**2
print(f"Su Indice de Masa Corporal es {imc:.2f} ")


