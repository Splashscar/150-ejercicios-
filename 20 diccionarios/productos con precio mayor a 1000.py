productos = {"laptop": 1500, "smartphone": 800, "tablet": 1200,}
for prod, valor in productos.items():
    if valor > 1000:
        print(prod, ":", valor)