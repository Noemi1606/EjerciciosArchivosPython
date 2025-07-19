with open('datos.txt', 'w', encoding='utf-8') as archivo:
    archivo.write("12\n")
    archivo.write("33\n")
    archivo.write("45\n")
    archivo.write("10\n")

def sumar_numeros(archivo):
    total = 0
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                numero = int(linea.strip())
                total += numero
        return total
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
        return 0
    except ValueError:
        print("El archivo contiene datos no válidos.")
        return 0

suma_total = sumar_numeros('datos.txt')
print(f"La suma total de los números es: {suma_total}")