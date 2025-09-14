import re 

def contar_frecuencia_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en el texto.
    Retorna un diccionario con la palabra y su frecuencia.
    """
    
    palabras = re.findall(r'\b\w+\b', texto.lower())
    
  
    frecuencias = {}
    print("--- Proceso de conteo de palabras ---")
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
            print(f"  > Palabra '{palabra}' encontrada de nuevo. Frecuencia: {frecuencias[palabra]}")
        else:
            frecuencias[palabra] = 1
            print(f"  > Nueva palabra encontrada: '{palabra}'")
            
    return frecuencias

def analizar_estructura(texto):
    """Analiza la estructura básica del texto"""
    estadisticas = {
        'caracteres_total': len(texto),
        'caracteres_sin_espacios': len(texto.replace(' ', '')),
        'palabras': len(re.findall(r'\b\w+\b', texto)),
        'oraciones': len([s for s in texto.split('.') if s.strip()]),
        'párrafos': len([p for p in texto.split('\n\n') if p.strip()])
    }
    return estadisticas

def mostrar_reporte_frecuencias(frecuencias):
    """
    Muestra un reporte detallado de la frecuencia de palabras.
    """
    if not frecuencias:
        print("El texto está vacío o no contiene palabras.")
        return
        
    print("\n" + "=" * 40)
    print("REPORTE DE FRECUENCIA DE PALABRAS")
    print("=" * 40)
    

    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    
    for palabra, frecuencia in frecuencias_ordenadas:
        print(f" - '{palabra}': {frecuencia} veces")
    
    print("-" * 40)
    

def analizar_texto_completo(texto):
    """Realiza un análisis completo del texto, incluyendo la frecuencia de palabras."""
    print("ANÁLISIS DE TEXTO COMPLETO")
    print("=" * 30)

   
    estadisticas = analizar_estructura(texto)
    print("\nEstadísticas del texto:")
    for clave, valor in estadisticas.items():
        print(f" - {clave}: {valor}")
    
   
    frecuencias = contar_frecuencia_palabras(texto)
    
    
    mostrar_reporte_frecuencias(frecuencias)


texto_ejemplo = """
El veloz zorro marrón salta sobre el perro perezoso.
Este zorro es muy astuto y el perro es muy perezoso.
Este es un ejemplo de un texto.
"""

analizar_texto_completo(texto_ejemplo)