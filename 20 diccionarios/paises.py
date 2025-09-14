paises = {"Colombia": "Bogotà", "Francia": "París", "Italia": "Roma"}
pais = input("Ingrese el nombre de un país: ")
print("La capital de", pais, "es", paises.get(pais, "Desconocida"))