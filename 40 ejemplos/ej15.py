numero_secret=17
intentosmaximos=3
intentos=1 
print("Adivina el número que estoy pensando del 1 al 20. Tienes", intentosmaximos, "intentos.")
while intentos <= intentosmaximos:
    numeroescogido=int(input("Intento " + str(intentos) + ": "))
    if numeroescogido == numero_secret:
        print("¡Felicidades! ¡Has adivinado el número!")
        break
    elif numeroescogido < numero_secret:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")
    intentos += 1
if intentos > intentosmaximos:
    print("Lo siento, has agotado tus intentos. El número era:", numero_secret)
print("¡Gracias por jugar!")