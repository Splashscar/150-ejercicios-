class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.id_producto}: {self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"

class Tienda:
    def __init__(self):
        self.inventario = []
        self.carrito = {}

    def agregar_producto(self, producto):
        self.inventario.append(producto)

    def mostrar_inventario(self):
        print("\n--- Inventario ---")
        for producto in self.inventario:
            print(producto)

    def agregar_al_carrito(self):
        self.mostrar_inventario()
        try:
            id_prod = input("Ingrese el ID del producto que desea agregar al carrito: ")
            producto = next((p for p in self.inventario if p.id_producto == id_prod), None)
            if not producto:
                print("Producto no encontrado.")
                return
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad <= 0:
                print("Cantidad inválida.")
                return
            if cantidad > producto.stock:
                print("No hay suficiente stock.")
                return

            if id_prod in self.carrito:
                self.carrito[id_prod]['cantidad'] += cantidad
            else:
                self.carrito[id_prod] = {'producto': producto, 'cantidad': cantidad}

            print(f"{cantidad} unidad(es) de {producto.nombre} agregada(s) al carrito.")
        except ValueError:
            print("Entrada inválida.")

    def mostrar_carrito(self):
        print("\n--- Carrito de Compras ---")
        if not self.carrito:
            print("El carrito está vacío.")
            return
        total = 0
        for item in self.carrito.values():
            prod = item['producto']
            cant = item['cantidad']
            subtotal = prod.precio * cant
            total += subtotal
            print(f"{prod.nombre} x{cant} = ${subtotal:.2f}")
        print(f"Total a pagar: ${total:.2f}")

    def procesar_pedido(self):
        if not self.carrito:
            print("El carrito está vacío. Agrega productos primero.")
            return
        print("\nProcesando pedido...")
        total = 0
        for item in self.carrito.values():
            prod = item['producto']
            cant = item['cantidad']
            prod.stock -= cant
            total += prod.precio * cant
        self.carrito.clear()
        print(f"Pedido procesado correctamente. Total pagado: ${total:.2f}")

def menu():
    tienda = Tienda()

    # Agregar productos iniciales
    tienda.agregar_producto(Producto("P001", "Camiseta", 15.99, 10))
    tienda.agregar_producto(Producto("P002", "Jeans", 39.99, 5))
    tienda.agregar_producto(Producto("P003", "Zapatos", 59.99, 3))
    tienda.agregar_producto(Producto("P004", "Gorra", 9.99, 8))

    while True:
        print("\n1. Mostrar inventario")
        print("2. Agregar producto al carrito")
        print("3. Mostrar carrito")
        print("4. Procesar pedido")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            tienda.mostrar_inventario()
        elif opcion == '2':
            tienda.agregar_al_carrito()
        elif opcion == '3':
            tienda.mostrar_carrito()
        elif opcion == '4':
            tienda.procesar_pedido()
        elif opcion == '5':
            print("Gracias por visitar la tienda. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
