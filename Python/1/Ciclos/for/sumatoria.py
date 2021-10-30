suma = 0
for i in range(1, 5):
    suma+= i*(1+i)
    
print(f"Ejercicio 1: {suma}") 

suma2 = 0
for i in range(-1, 1):
    suma2+=2**i*(3+i)
    
print(f"Ejercicio 2: {suma2}") 

suma3 = 0
for i in range(1, 101):
    suma3+=1/i
    
print(f"Ejercicio 3: {suma3:.2f}") 