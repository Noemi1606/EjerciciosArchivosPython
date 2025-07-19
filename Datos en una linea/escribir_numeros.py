numeros = [10, 20, 30, 40, 50]


with open('numeros.txt', 'w', encoding='utf-8') as archivo:
    for numero in numeros:
        archivo.write(str(numero) + '\n') 


print("Se escribió cada número en una línea en 'numeros.txt'.")