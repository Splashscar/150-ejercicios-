import random
import math
from itertools import permutations
def calcular_distancia(ciudad1, ciudad2):
    """
    Calcula la distancia euclidiana entre dos ciudades
    Cada ciudad tiene coordenadas (x, y)
    """
    x1, y1 = ciudad1
    x2, y2 = ciudad2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distancia, 2)
def calcular_distancia_total_ruta(ciudades, ruta):
    """
    Calcula la distancia total de una ruta completa
    La ruta es una lista de índices de ciudades
    """
    distancia_total = 0
    # Calcular distancia entre ciudades consecutivas
    for i in range(len(ruta)):
        ciudad_actual = ciudades[ruta[i]]
        siguiente_ciudad = ciudades[ruta[(i + 1) % len(ruta)]] # % para volver al inicio
        distancia = calcular_distancia(ciudad_actual, siguiente_ciudad)
        distancia_total += distancia
    return round(distancia_total, 2)
def metodo_fuerza_bruta(ciudades):
    """
    Encuentra la ruta óptima probando todas las combinaciones posibles
    ¡ADVERTENCIA: Solo usar con pocas ciudades (f8) por complejidad computacional!
    """
    num_ciudades = len(ciudades)
print(f"")