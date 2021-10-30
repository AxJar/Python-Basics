"""Programa que pide una distancia en centímetros y devuelve esa distancia en su equivalente en kilómetros, metros y centímetros
(escribiendo solamente las unidades necesarias).
"""
cm = int(input("Dame tu distancia en centímetros: "))
km = cm/100000
m = cm/100
cm2 = cm%100
if km >= 1:
    print(int(km), "km")
if (m-(int(km)*1000)) >= 1:
    print (int(m)-(int(km)*1000), "m")
if not(cm%100 == -0):
    print(int(cm2), "cm")