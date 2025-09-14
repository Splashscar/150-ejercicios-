def generar_y_procesar_cuadrados(numeros):
    """
    Toma una lista de números y genera sus cuadrados de forma detallada.
    """
    lista_cuadrados = []
    print(f"Analizando los números: {numeros}")
    print("-" * 40)
    
    for numero in numeros:
        cuadrado = numero ** 2
        lista_cuadrados.append(cuadrado)
        
        
        print(f"Número '{numero}':")
        print(f"  > Calculando su cuadrado: {numero} x {numero} = {cuadrado}")
        
    return lista_cuadrados

def verificar_paridad_cuadrado(numero, cuadrado):
    """
    Verifica si un número y su cuadrado tienen paridad (par/impar) similar.
    """
    es_par = "par" if numero % 2 == 0 else "impar"
    cuadrado_es_par = "par" if cuadrado % 2 == 0 else "impar"
    
    return f"  > El número es {es_par} y su cuadrado es {cuadrado_es_par}"

def mostrar_reporte_final(numeros_originales, cuadrados):
    """
    Muestra un reporte final con los números y sus cuadrados.
    """
    print("\n" + "=" * 40)
    print("REPORTE DE GENERACIÓN DE CUADRADOS")
    print("=" * 40)
    
    for i in range(len(numeros_originales)):
        numero = numeros_originales[i]
        cuadrado = cuadrados[i]
        
        print(f"\nNúmero: {numero}")
        print(f"Cuadrado: {cuadrado}")
        print(verificar_paridad_cuadrado(numero, cuadrado))
        print("-" * 25)


print("GENERADOR DE CUADRADOS")
print("=" * 25)


numeros = [1, 2, 3, 4, 5, 6]


cuadrados_generados = generar_y_procesar_cuadrados(numeros)


mostrar_reporte_final(numeros, cuadrados_generados)