# inicializaciones
suma = 0
num = int(input("Cuantas calificaciones me vas a dar a promediar: "))

# con for NO necesito contador, i hace las veces de contador
for i in range(num):
    calif = float(input(f"Dame la calificacion {i+1}: "))
    suma = suma+calif


# con while
# necesito contador
# cont=1
# while cont<=num:
#   calif=float(input(f"Dame la calificacion {cont}: "))
#  suma=suma+calif
# cont=cont+1 #necesito incrementar el contador

promedio = suma/num
print(f"El promedio de las calificaciones es {promedio:.2f}")