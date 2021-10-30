suma = 0
divisor = 1
num = int(input())
if num > 0:
    while divisor < num:
        if num % divisor == 0:
            suma += divisor
        divisor += 1
    if suma == num:
        print("El numero es perfecto")
    else:
        print("El numero no es perfecto")