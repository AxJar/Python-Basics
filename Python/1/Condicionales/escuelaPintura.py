'''
ENTRADAS:
numero de horas por semana
dia del mes que se paga la mensualidad
SALIDAS:
monto a pagar por la mensualidad
'''
print("Teclea el numero de horas por semana que tomas la clase" )
horas_semana = int(input())
print("Teclea el dia del mes en el que realizaras el pago" )
dia = int(input())

if horas_semana == 1:
    costo = 700
else:
    costo = 1200

if dia <= 5:
    desc = costo*0.10
    costo = costo-desc

print(f"El pago de la mensualidad sera de {costo}")

