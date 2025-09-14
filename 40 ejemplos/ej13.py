sumatot=0
numeroact=1
limite=int(input("¿Hasta qué número quieres sumar? "))
while numeroact <= limite:
    sumatot += numeroact
    print("Número actual:", numeroact)
    numeroact += 1
print("La suma total desde 1 hasta", limite, "es:", sumatot)
print("¡He terminado de sumar!")