"""Este programa convierte una cantidad dada en pesos a dolares.
Autor:Axel Jarquin Morga
ENTRADAS: pesos, tipo_cambio
PROCESO: Solicito la cantidad de pesos a convertir y se guarda en pesos
         Solicito el tipo de cambio y se guarda en su variable
         Divido pesos entre el tipo de cambio
         Imprimo el resultado
SALIDA:usd
"""
print("Este programa convierte una cantidad dada en pesos a dolares")
pesos = float(input("Dame la cantidad de pesos a cambiar "))
tipo_cambio = float(input("Cuanto vale el dolar el dia de hoy? "))
usd = pesos/tipo_cambio
print(f" ${pesos:.2f} pesos, al tipo de cambio de ${tipo_cambio:.2f}, seran ${usd:.2f} dolares ")
