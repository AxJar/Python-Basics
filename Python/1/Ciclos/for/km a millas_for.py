'''
km a millas
'''
def km_millas(km):
    milla = km*0.6213
    return milla

print("Este programa convierte el numero de km en millas")
num = int(input("Hasta que numero de km quieres ver: "))
print("kms \t millas")
for i in range (1, num+1):
    millas = km_millas(i)
    print(f"{i} \t {millas:.4f}")
