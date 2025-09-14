precio_total = int(input("Ingrese el precio total de su compra: $"))
descuento = 0 

if precio_total > 100: 
    descuento = precio_total * 0.10 
    precio_final = precio_total - descuento
    print("Tienes un descuento del 10% :)")
    print("Descuento aplicado: $", descuento)
    print("Precio final: $", precio_final)
    
else:
    precio_final = precio_total
    print("No hay descuento disponible")
    print("Precio original: $", precio_total)
    print("Precio final: $", precio_final)