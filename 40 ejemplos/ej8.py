Nota1=int(input("Ingrese la primera calificación: "))
Nota2=int(input("Ingrese la segunda calificación: "))
Nota3=int(input("Ingrese la tercera calificación: "))

sum = Nota1 + Nota2 + Nota3 
promedio = sum / 3 
print("Calificaciones:", Nota1, Nota2, Nota3)
print("Promedio:", promedio)
if promedio >= 7:
    print("¡genial!, aprobaste.")
elif promedio >= 5:
    print("Pasaste, pero pudo haber estado mejor.")
else:
    print("Reprobaste, mejor suerte la próxima vez.")   