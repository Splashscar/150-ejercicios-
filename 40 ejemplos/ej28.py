def calcular_potencia(base, exponente):
  
    if exponente == 0:
        return 1, 0
    if exponente < 0:
        print("✗ No se admite exponente negativo en esta versión.")
        return None, 0

    resultado = 1
    multiplicaciones = 0
    
    print(f"Calculando {base} elevado a la {exponente}")
    print("\nProceso paso a paso:")

   
    for i in range(exponente):
        multiplicaciones += 1
        resultado *= base
        print(f"  Multiplicación {multiplicaciones}: resultado parcial = {resultado}")

    return resultado, multiplicaciones

def mostrar_estadisticas_potencia(base, exponente, resultado, multiplicaciones):
    """Muestra estadísticas detalladas del cálculo."""
    print("\n" + "=" * 40)
    print("ESTADÍSTICAS DEL CÁLCULO DE POTENCIA")
    print("=" * 40)
    print(f"Base: {base}")
    print(f"Exponente: {exponente}")
    print(f"Resultado final: {resultado}")
    print(f"Total de multiplicaciones realizadas: {multiplicaciones}")


print("CALCULADORA DE POTENCIA")
print("=" * 30)

base_ejemplo = 2
exponente_ejemplo = 5
resultado_ejemplo, mult_ejemplo = calcular_potencia(base_ejemplo, exponente_ejemplo)
if resultado_ejemplo is not None:
    mostrar_estadisticas_potencia(base_ejemplo, exponente_ejemplo, resultado_ejemplo, mult_ejemplo)

print("\n" + "=" * 50)
base_ejemplo2 = 3
exponente_ejemplo2 = 4
resultado_ejemplo2, mult_ejemplo2 = calcular_potencia(base_ejemplo2, exponente_ejemplo2)
if resultado_ejemplo2 is not None:
    mostrar_estadisticas_potencia(base_ejemplo2, exponente_ejemplo2, resultado_ejemplo2, mult_ejemplo2)