'''Este programa calculara la cantidad de billetes y monedas que se necesitan para cubrir la cantidad dada por el usuario.
AUTOR:Axel Jarquin Morga
ENTRADA: total_dinero
PROCESO: Solicitar la cantidad de dinero que el usuario desea retirar y guardarla en la variable
correspondiente.
Dividir la cantidad de dinero total entre  200 y obtener el sobrante
Dividir el sobrante entre 50 y obtener sobrante
Dividir el sobrante  entre 20 y obtener  sobrante.
Dividir sobrante entre 1
Imprimir el resultado
SALIDA:
'''
print(" Este programa calculara la cantidad de billetes de 200, 50, 20 y monedas den 1 peso que va a retirar")
dinero_total = int(input("Ingrese la cantidad de dinero que desea retirar "))
billete_200 = dinero_total//200
sob_billete200 = dinero_total%200
billete_50 = sob_billete200//50
sob_billete50 = sob_billete200%50
billete_20 = sob_billete50//20
moneda1peso = sob_billete50%20
print("Para ", dinero_total, ", pesos se necesitan ", billete_200, " billete(s) de 200, ", billete_50, " billete(s) de 50 y "
      , billete_20, " billete(s) de 20 con ", moneda1peso, " moneda(s) de 1 peso")
