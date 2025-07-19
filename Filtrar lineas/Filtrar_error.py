with open('log.txt', 'w', encoding='utf-8') as archivo:
    archivo.write("INFO: Usuario inició sesión\n")
    archivo.write("ERROR: No se pudo cargar el perfil\n")
    archivo.write("WARNING: Espacio en disco casi lleno\n")
    archivo.write("ERROR: Fallo de autenticación\n")
    archivo.write("INFO: Configuración guardada\n")
    archivo.write("ERROR: Archivo dañado\n")

with open('log.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        if 'ERROR' in linea:
            print(linea.strip())