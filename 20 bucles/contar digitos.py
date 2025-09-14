num = 123456
contador = 0
while num > 0:
    num //= 10
    contador += 1
print("El número tiene", contador, "dígitos")