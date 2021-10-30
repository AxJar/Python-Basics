"""
Programa para practicar acumulador y contador
Los ahorros de Juanita

"""
suma = 0 #Va a ser mi acumulador , esta vacio , debe inicializarse en 0
dias = 1 #Inicia contando en 1
while dias <= 7:
    ahorro = float(input(f"Dime cuanto ahorraste el dia {dias}: "))
    suma = suma+ahorro
    dias = dias+1
print(f"El total ahorrado es ${suma:.2f}")


