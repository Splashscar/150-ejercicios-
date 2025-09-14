lista = [3, 5, 7, 9, 11, 13, 15]
buscar = int(input("Ingrese un numero a buscar: "))
encontrado = False
for n in lista:
    if n == buscar:
        encontrado = True
        break
print("El numero", buscar, "si" if encontrado else "no", "se encuentra en la lista.")