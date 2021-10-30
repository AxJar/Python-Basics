def verifica_calif(calif):
    if calif >= 0 and calif <= 100:
        return True
    else:
        return False

def main():
    calif1 = int(input())
    calif2 = int(input())
    calif3 = int(input())

    if verifica_calif(calif1) == True and verifica_calif(calif2) == True and verifica_calif(calif3) == True:
        promedio = (calif1 + calif2 + calif3) / 3
        print(f"El promedio es {promedio}")
    else:
        print("Todas las calificaciones deben ser valores entre 0 y 100")

main()