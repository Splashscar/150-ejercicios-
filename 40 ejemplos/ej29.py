def encontrar_minimo_paso_a_paso(lista):
    """
    Busca el valor mínimo en una lista y muestra cada comparación.
    """
    if not lista:
        return None, 0
    
    minimo_actual = lista[0]
    comparaciones = 0
    print(f"\nBuscando el valor mínimo en: {lista}")
    print(f"Valor inicial de mínimo: {minimo_actual}")
    
    for i in range(1, len(lista)):
        comparaciones += 1
        elemento = lista[i]
        print(f"  Comparación {comparaciones}: ¿Es {elemento} menor que {minimo_actual}?")
        if elemento < minimo_actual:
            minimo_actual = elemento
            print(f"  ✓ Sí. Nuevo mínimo encontrado: {minimo_actual}")
        else:
            print("  ✗ No. El mínimo actual sigue siendo el mismo.")
    
    return minimo_actual, comparaciones

def encontrar_maximo_paso_a_paso(lista):
    """
    Busca el valor máximo en una lista y muestra cada comparación.
    """
    if not lista:
        return None, 0
        
    maximo_actual = lista[0]
    comparaciones = 0
    print(f"\nBuscando el valor máximo en: {lista}")
    print(f"Valor inicial de máximo: {maximo_actual}")
    
    for i in range(1, len(lista)):
        comparaciones += 1
        elemento = lista[i]
        print(f"  Comparación {comparaciones}: ¿Es {elemento} mayor que {maximo_actual}?")
        if elemento > maximo_actual:
            maximo_actual = elemento
            print(f"  ✓ Sí. Nuevo máximo encontrado: {maximo_actual}")
        else:
            print("  ✗ No. El máximo actual sigue siendo el mismo.")
    
    return maximo_actual, comparaciones

def mostrar_estadisticas_busqueda(minimo, maximo, comp_min, comp_max, total_elementos):
    """Muestra estadísticas del proceso de búsqueda."""
    print("\n" + "=" * 40)
    print("ESTADÍSTICAS DE BÚSQUEDA")
    print("=" * 40)
    print(f"Total de elementos analizados: {total_elementos}")
    print(f"Valor mínimo encontrado: {minimo} (en {comp_min} comparaciones)")