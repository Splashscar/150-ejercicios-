import random
secreto = random.randint(1, 10)
intento = int(input("Adivina el número entre 1 y 10: "))
while intento != secreto:
    intento = int(input("Incorrecto. Intenta de nuevo: "))
print("¡Felicidades! ¡Has adivinado el número!")