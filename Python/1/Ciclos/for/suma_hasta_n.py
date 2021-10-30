"""Programa que lee un número entero positivo n, después debe calcular la suma 1+2+3+...+n.
Finalmente muestre el resultado de la suma en pantalla. """

x = int(input())
sum = 0
for num in range(x+1):
    sum = sum+num
print(sum)
