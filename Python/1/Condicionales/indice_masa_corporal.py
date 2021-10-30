"""Programa que calcula el IMC (Indice de Masa Corporal) de una persona, el cual se utiliza para determinar si la proporción de peso y altura es adecuada.
Rango de índice Descripción
índice < 20 'PESO BAJO'
20 <= índice < 25 'NORMAL'
25 <= índice < 30 'SOBREPESO'
30 <= índice < 40 'OBESIDAD'
40 >= índice 'OBESIDAD MORBIDA'"""

peso = float(input("Cual es tu peso en kilogramos: "))
estatura = float(input("Cual es tu estatura en metros: "))
imc = peso/estatura**2
if imc < 20:
    print("PESO BAJO")
elif imc <= 25:
    print("NORMAL")
elif imc <= 30:
    print("SOBREPESO")
elif imc < 40:
    print("OBESIDAD")
elif imc >= 40:
    print("OBESIDAD MÓRBIDA")
    
