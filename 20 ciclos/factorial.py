n = int(input("Ingrese un numero: "))
fact = 1
i = 1
while 1 <= n:
    fact *= i
    i += 1
print("El factorial de", n, "es:", fact)