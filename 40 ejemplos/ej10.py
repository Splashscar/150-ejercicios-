contraseña=str(input("Ingrese la contraseña: "))
contraseña_minima=8
print("La contraseña tiene", len(contraseña), "caracteres")
if len(contraseña) >= contraseña_minima:
    print("Contraseña válida")
else:  
    print("Contraseña inválida, debe tener al menos", contraseña_minima, "caracteres")    