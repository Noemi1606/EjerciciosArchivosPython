
def contar_palabras(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            palabras = contenido.split()
            return len(palabras)
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return 0

archivo = 'frases.txt'
total = contar_palabras(archivo)
print(f"Total de palabras en el archivo: {total}")