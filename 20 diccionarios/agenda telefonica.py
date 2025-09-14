agenda = {"Juan": "1234", "María": "9876", "Pedro": "5556"}
nombre = input("Ingrese el nombre a buscar: ")
print("El número de teléfono es:", agenda.get(nombre, "No encontrado"))