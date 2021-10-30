'''Este programa calcula el tiempo promedio que una persona tarda en recorrer
su ruta en cualquier semana, segun los datos de tiempo por dia que corra, que proporcione
el usuario.
AUTOR:Axel Jarquin Morga
ENTRADAS: tiempoLunes, tiempoMiercoles, TiempoViernes
PROCESO: Se piden los diferentes tiempos de los dias de la semana que la persona recorre
la misma ruta y se guardan en las variables correspondientes. Se suman las 3 variables y
se dividen entre 3, despues se imprime el resultado.
SALIDAS:promedio
'''
print("Este programa calcula el tiempo promedio en horas, que una persona tarda en recorrer su ruta en cualquier semana")
tiempoLunes = float(input("Dame el tiempo, en horas, que tardas en recorrer tu ruta el lunes "))
tiempoMiercoles = float(input("Dame el tiempo, en horas, que tardas en recorrer tu ruta el miercoles "))
TiempoViernes = float(input("Dame el tiempo, en horas , que tardas en recorrer tu ruta el viernes "))
promedio = (tiempoLunes+tiempoMiercoles+TiempoViernes)/3 #Uso parentesis para realizar primero la suma y despues la division
print(f"Tu tiempo promedio que tardas en recorrer tu ruta en una semana es {promedio:.2f} horas")


