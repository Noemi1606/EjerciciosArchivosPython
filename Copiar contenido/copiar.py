def copiar_contenido(archivo_origen, archivo_destino):
    try:
        with open(archivo_origen, 'r', encoding='utf-8') as origen:
            contenido = origen.read()
        
        with open(archivo_destino, 'w', encoding='utf-8') as destino:
            destino.write(contenido)
        
        print(f"Contenido copiado de '{archivo_origen}' a '{archivo_destino}' correctamente.")
    except FileNotFoundError:
        print("El archivo origen no fue encontrado.")


copiar_contenido('origen.txt', 'copia.txt')