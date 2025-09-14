intentos = 0
num = int(input("Ingrese un numero: "))
while num != 5:
    intentos += 1
    num = int(input("Ingrese un numero: "))
print("Cantidad de intentos:", intentos)