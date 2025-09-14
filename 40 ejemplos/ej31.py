import random
import string

class Animal:
    def __init__(self, nombre, tipo, energia=100, posicion_x=0, posicion_y=0):
        self.nombre = nombre
        self.tipo = tipo  
        self.energia = energia
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.vivo = True

    def mover(self):
        """Mueve el animal aleatoriamente y consume energía."""
        if self.vivo:
            self.posicion_x += random.randint(-1, 1)
            self.posicion_y += random.randint(-1, 1)
            self.energia -= 5  
            print(f"³ {self.nombre} se movió. Energía actual: {self.energia}")
            if self.energia <= 0:
                self.vivo = False
                print(f"✗ ¡{self.nombre} se quedó sin energía y ha muerto!")
        else:
            print(f"✗ {self.nombre} está muerto. No puede moverse.")
    
    def buscar_alimento(self, entorno):
        """Busca alimento en el entorno, basado en su tipo de dieta."""
        if not self.vivo:
            print(f"✗ {self.nombre} no puede buscar alimento, ya está muerto.")
            return

        print(f"\nBuscando alimento en el entorno: {entorno}")
        
      
        if self.tipo == "herbívoro":
            comida_ideal = "hierba"
            if comida_ideal in entorno.lower():
                print(f"✓ ¡{self.nombre} (herbívoro) encontró {comida_ideal}!")
                return True
            else:
                print(f"✗ {self.nombre} no encontró {comida_ideal} en el entorno.")
                return False
        
        elif self.tipo == "carnívoro":
            comida_ideal = "carne"
            if comida_ideal in entorno.lower():
                print(f"✓ ¡{self.nombre} (carnívoro) encontró {comida_ideal}!")
                return True
            else:
                print(f"✗ {self.nombre} no encontró {comida_ideal} en el entorno.")
                return False
        
        else:
            print(f"El tipo de animal {self.tipo} no es compatible.")
            return False

    def alimentar(self, cantidad):
        """Aumenta la energía del animal."""
        self.energia += cantidad
        print(f"³ {self.nombre} se alimentó. Energía actual: {self.energia}")

    def mostrar_estado(self):
        """Muestra el estado actual del animal."""
        estado = "Vivo" if self.vivo else "Muerto"
        print(f"\n--- Estado de {self.nombre} ---")
        print(f"Tipo: {self.tipo}")
        print(f"Estado: {estado}")
        print(f"Energía: {self.energia}")
        print(f"Posición: ({self.posicion_x}, {self.posicion_y})")
        print("-" * 30)


print("SIMULADOR DE ANIMALES")
print("=" * 25)


jirafa = Animal("Jirafa", "herbívoro", energia=80)
leon = Animal("León", "carnívoro", energia=90)


entorno_con_hierba = "Hay mucha hierba fresca y árboles altos."
entorno_con_carne = "Se puede sentir el olor a carne a lo lejos."
entorno_vacio = "El desierto está vacío, solo hay arena."


print("\n--- SIMULACIÓN DE LA JIRAFA ---")
jirafa.mostrar_estado()
jirafa.mover()
if jirafa.buscar_alimento(entorno_con_hierba):
    jirafa.alimentar(20)


print("\n--- SIMULACIÓN DEL LEÓN ---")
leon.mostrar_estado()
leon.mover()
if leon.buscar_alimento(entorno_con_carne):
    leon.alimentar(30)
else:
    leon.mover() 


print("\n--- SIMULACIÓN EN ENTORNO VACÍO ---")
jirafa.mostrar_estado()
leon.mostrar_estado()
jirafa.buscar_alimento(entorno_vacio)
leon.buscar_alimento(entorno_vacio)
jirafa.mover()
leon.mover()
jirafa.mostrar_estado()
leon.mostrar_estado()