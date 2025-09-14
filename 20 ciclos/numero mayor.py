n = int(input("Cuantos numeros ingresaras?: "))
mayor = None
for i in range (n):
    num = int(input("Numero: "))
    if mayor is None or num > mayor:
        mayor = num
print("El numero mayor es:", mayor)