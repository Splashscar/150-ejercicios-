numero_escogido=7
numero_a_escoger=int(input("Adivina el número que estoy pensando del 1 al 10: "))
if numero_escogido == numero_a_escoger:
    print("¡Felicidades! ¡Has adivinado el número!")
elif numero_escogido < numero_a_escoger:
    print("El número es mayor. Intenta de nuevo.")
else:
    print("El número es menor. Intenta de nuevo.")