calificaciones = [5.0, 6.5, 7.0, 8.5, 9.0]
tot_cal=len(calificaciones)
suma=sum(calificaciones)
promedio=suma/tot_cal
notamayor=max(calificaciones)
notamenor=min(calificaciones)
print("Calificaciones:", calificaciones)
print("Total de calificaciones:", tot_cal)
print("Suma de calificaciones:", suma)
print("Promedio de calificaciones:", promedio)
print("Calificación más alta:", notamayor)
print("Calificación más baja:", notamenor)
if promedio >= 7:
    print("¡Excelente rendimiento!")
else:
    print("Puedes mejorar tu rendimiento.")