# --- Ejercicio 1: Lectura de líneas de un archivo de texto 
with open('nombres.txt', 'w', encoding='utf-8') as f:
    f.write('Rosmery\n')
    f.write('Kiara\n')
    f.write('Kamil\n')
    f.write('Melissa\n')

print("--- Ejercicio 1: Lectura de nombres (actualizado) ---")
try:
    with open('nombres.txt', 'r', encoding='utf-8') as archivo:
        for nombre in archivo:
            print(nombre.strip()) # .strip() para eliminar los saltos de línea
except FileNotFoundError:
    print("El archivo 'nombres.txt' no se encontró.")