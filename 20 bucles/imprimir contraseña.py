password = "python123"
entrada = input("Ingresa la contraseña: ")
while entrada != password:
    print("Contraseña incorrecta. Intenta de nuevo.")
    entrada = input("Ingresa la contraseña: ")
print("¡Contraseña correcta!")