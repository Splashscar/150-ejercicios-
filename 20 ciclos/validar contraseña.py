password = "python123"
intentos = 0
while intentos < 3:
    clave = input("Ingresa la contraseña: ")
    if clave == password:
        print("¡Contraseña correcta!")
        break
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Te quedan {3 - intentos} intentos.")
else:
    print("Has excedido el número de intentos. Acceso bloqueado.")