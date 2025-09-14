suma = 0
for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    suma += nota   
print("El promedio de las notas es:", suma / 5)