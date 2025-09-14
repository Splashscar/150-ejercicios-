num = int(input("Ingrese un numero: "))
suma = 0
while num > 0:
    suma += num % 10
    num //= 10
print("Suma de los digitos: ", suma)