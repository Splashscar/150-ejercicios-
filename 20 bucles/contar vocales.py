texto = "Hola, ¿cómo estás?"
vocales = 0
for letra in texto.lower():
    if letra in "aeiouáéíóú":
        vocales += 1
print("Número de vocales:", vocales)