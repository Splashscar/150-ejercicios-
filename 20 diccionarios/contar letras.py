palabra = "banana"
conteo = {}
for letra in palabra:
    if letra in conteo:
        conteo[letra] += 1
    else:
        conteo[letra] = 1
print(conteo)