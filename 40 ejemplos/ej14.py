n=1
limit=100
pares= 0
while n <= limit:
    if n % 2 == 0:
        pares =pares + 1
    n += 1 
print("La suma de los números pares del 1 al 100 es:", pares)
print("¡He terminado de sumar los números pares!")