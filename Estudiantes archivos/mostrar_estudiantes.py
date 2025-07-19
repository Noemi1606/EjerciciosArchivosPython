with open('estudiantes.csv', 'w', encoding='utf-8') as archivo:
    archivo.write("nombre,edad,calificacion\n")
    archivo.write("Noemi,20,85\n")
    archivo.write("Mateo,21,90\n")
    archivo.write("Ramcel,19,95\n")

with open('estudiantes.csv', 'r', encoding='utf-8') as archivo:
    next(archivo)  # Saltar la primera línea (encabezados)
    for linea in archivo:
        nombre, edad, calificacion = linea.strip().split(',')
        print(f"{nombre} tiene {edad} años y obtuvo una calificación de {calificacion}")