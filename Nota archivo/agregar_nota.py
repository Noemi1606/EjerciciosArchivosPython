nota = input("Escribe una nota: ")

with open('notas.txt', 'a', encoding='utf-8') as archivo:
    archivo.write(nota + '\n')

print("La nota fue guardada exitosamente.")