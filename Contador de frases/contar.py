
def contar_palabras(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            return len(palabras)
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return 0

archivo = 'frases.txt'
total = contar_palabras(archivo)
print(f"Total de palabras en el archivo: {total}")