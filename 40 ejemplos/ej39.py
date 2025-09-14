def inicio():
    print("\nTe despiertas en un bosque oscuro y misterioso.")
    print("Hay dos caminos frente a ti:")
    print("1. Tomar el camino a la izquierda.")
    print("2. Tomar el camino a la derecha.")

    eleccion = input("¿Qué eliges? (1/2): ")

    if eleccion == '1':
        cueva()
    elif eleccion == '2':
        rio()
    else:
        print("Opción no válida. Intenta de nuevo.")
        inicio()

def cueva():
    print("\nLlegas a la entrada de una cueva oscura.")
    print("¿Quieres entrar o regresar?")
    print("1. Entrar en la cueva.")
    print("2. Regresar al bosque.")

    eleccion = input("¿Qué eliges? (1/2): ")

    if eleccion == '1':
        dentro_cueva()
    elif eleccion == '2':
        inicio()
    else:
        print("Opción no válida. Intenta de nuevo.")
        cueva()

def dentro_cueva():
    print("\nDentro de la cueva encuentras un cofre brillante.")
    print("¿Quieres abrirlo o salir corriendo?")
    print("1. Abrir el cofre.")
    print("2. Salir corriendo.")

    eleccion = input("¿Qué eliges? (1/2): ")

    if eleccion == '1':
        print("\n¡Encontraste un tesoro! Eres rico y feliz. ¡Fin del juego!")
    elif eleccion == '2':
        print("\nTe tropiezas al salir y te lastimas. Fin del juego.")
    else:
        print("Opción no válida. Intenta de nuevo.")
        dentro_cueva()

def rio():
    print("\nLlegas a un río caudaloso.")
    print("Hay un puente viejo y una barca.")
    print("1. Cruzar el puente.")
    print("2. Usar la barca para cruzar.")

    eleccion = input("¿Qué eliges? (1/2): ")

    if eleccion == '1':
        puente()
    elif eleccion == '2':
        barca()
    else:
        print("Opción no válida. Intenta de nuevo.")
        rio()

def puente():
    print("\nEl puente cruje y se rompe mientras cruzas.")
    print("Te caes al agua y no puedes salir. Fin del juego.")

def barca():
    print("\nNavegas con cuidado y llegas a una aldea segura.")
    print("¡Felicidades! Has encontrado un nuevo hogar. Fin del juego.")

if __name__ == "__main__":
    inicio()
