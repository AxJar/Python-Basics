""" Una persona puede obtener su licencia de manejo si es mayor de edad y tiene identificación oficial
Programa que lee la edad de una persona y si tiene (s/n) identificación oficial
De salida debe mostrar Si si puede obtener su licencia o No si no la puede obtener """

edad = int(input("Cual es tu edad "))
licencia = str(input("Cuentas con una identificación oficial? "))

if edad >= 18 and str(licencia) == "s":
    print("Si puedes obtener tu licencia de manejo")
elif edad < 18 and str(licencia) == "s":
    print("No puedes obtener tu licencia de manejo")
elif edad >= 18 and str(licencia) == "n":
    print("No puedes obtener tu licencia de manejo")
elif  edad < 18 and str(licencia) == "n":
    print("No puedes obtener tu licencia de manejo")
