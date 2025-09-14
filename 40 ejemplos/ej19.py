animales =  ["perro", "gato", "elefante", "tigre", "león"]
print("Lista original de animales:", animales)
animal_buscado=str(input("Ingrese el nombre del animal que desea buscar: "))
if animal_buscado in animales:
    print(animal_buscado, "está en la lista de animales.")
    posicion = animales.index(animal_buscado)
    print("Posición de", animal_buscado, "en la lista:", posicion)
    cantidad = animales.count(animal_buscado)
    print("Cantidad de veces que aparece", animal_buscado, "en la lista:", cantidad)
else:
    print(animal_buscado, "no está en la lista de animales.")

buscados=["gato", "león", "jirafa"]
for animal in buscados:
    if animal in animales:
        print(animal, "está en la lista de animales.")
    else:
        print(animal, "no está en la lista de animales.")