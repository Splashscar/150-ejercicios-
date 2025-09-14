from datetime import datetime, timedelta

class Libro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn}) [{estado}]"

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = False

    def __str__(self):
        estado = "Devuelto" if self.devuelto else "En préstamo"
        return (f"Libro: {self.libro.titulo}, Usuario: {self.usuario.nombre}, "
                f"Préstamo: {self.fecha_prestamo.strftime('%Y-%m-%d')}, "
                f"Devolución: {self.fecha_devolucion.strftime('%Y-%m-%d')} [{estado}]")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self):
        isbn = input("ISBN: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        libro = Libro(isbn, titulo, autor)
        self.libros.append(libro)
        print("Libro agregado correctamente.")

    def agregar_usuario(self):
        id_usuario = input("ID usuario: ")
        nombre = input("Nombre: ")
        usuario = Usuario(id_usuario, nombre)
        self.usuarios.append(usuario)
        print("Usuario agregado correctamente.")

    def prestar_libro(self):
        isbn = input("ISBN del libro a prestar: ")
        libro = next((l for l in self.libros if l.isbn == isbn), None)
        if not libro:
            print("Libro no encontrado.")
            return
        if not libro.disponible:
            print("Libro no está disponible.")
            return

        id_usuario = input("ID del usuario: ")
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if not usuario:
            print("Usuario no encontrado.")
            return

        fecha_prestamo = datetime.now()
        dias_prestamo = int(input("Días de préstamo: "))
        fecha_devolucion = fecha_prestamo + timedelta(days=dias_prestamo)

        prestamo = Prestamo(libro, usuario, fecha_prestamo, fecha_devolucion)
        self.prestamos.append(prestamo)
        libro.disponible = False
        print(f"Préstamo registrado. Devolver antes de {fecha_devolucion.strftime('%Y-%m-%d')}")

    def devolver_libro(self):
        isbn = input("ISBN del libro a devolver: ")
        prestamo = next((p for p in self.prestamos if p.libro.isbn == isbn and not p.devuelto), None)
        if not prestamo:
            print("Préstamo no encontrado o libro ya devuelto.")
            return

        prestamo.devuelto = True
        prestamo.libro.disponible = True
        print(f"Libro '{prestamo.libro.titulo}' devuelto por {prestamo.usuario.nombre}.")

    def listar_libros(self):
        print("\n--- Libros en Biblioteca ---")
        for libro in self.libros:
            print(libro)

    def listar_usuarios(self):
        print("\n--- Usuarios Registrados ---")
        for usuario in self.usuarios:
            print(usuario)

    def listar_prestamos(self):
        print("\n--- Préstamos ---")
        for prestamo in self.prestamos:
            print(prestamo)

def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n1. Agregar libro")
        print("2. Agregar usuario")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Listar libros")
        print("6. Listar usuarios")
        print("7. Listar préstamos")
        print("8. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            biblioteca.agregar_libro()
        elif opcion == '2':
            biblioteca.agregar_usuario()
        elif opcion == '3':
            biblioteca.prestar_libro()
        elif opcion == '4':
            biblioteca.devolver_libro()
        elif opcion == '5':
            biblioteca.listar_libros()
        elif opcion == '6':
            biblioteca.listar_usuarios()
        elif opcion == '7':
            biblioteca.listar_prestamos()
        elif opcion == '8':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
