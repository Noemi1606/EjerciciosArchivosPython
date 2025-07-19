with open('poema.txt', 'w', encoding='utf-8') as archivo:
    archivo.write("El sol se asoma en la mañana,\n")
    archivo.write("las aves cantan con emoción,\n")
    archivo.write("un nuevo día se levanta,\n")
    archivo.write("lleno de luz e inspiración.\n")

with open('poema.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()
    cantidad = len(lineas)

print(f"El archivo tiene {cantidad} líneas.")