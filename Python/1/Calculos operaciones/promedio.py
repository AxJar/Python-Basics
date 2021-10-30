'''
Este programa saca el promedio de calificaciones del semestre pasado.
Autor:Axel Jarquin Morga
ENTRADA:cal1, cal2, cal3
PROCESO: Se pide cada una de las calificaciones y se guardan en la variable correspondiente.Sumo todas las calificaciones y las divido en 3
         despues imprimo el resultaddo
SALIDA:promedio
'''
print("Este programa saca el promedio de calificaciones de tu semestre pasado")
cal1 = float(input("Dame una calificacion "))
cal2 = float(input("Dame otra calificacion "))
cal3 = float(input("Dame la ultima calificacion "))
promedio = (cal1+cal2+cal3)/3 #Uso parentesis para realizar primero la suma y despues la division
print(f"Tu promedio fue {promedio:.4f}")
