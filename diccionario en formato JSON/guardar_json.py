import json

persona = {
    "nombre": "Kamil",
    "edad": 12,
    "ciudad": "Santo Domingo"
}

with open('persona.json', 'w', encoding='utf-8') as archivo:
    json.dump(persona, archivo, ensure_ascii=False, indent=4)

print("Diccionario guardado en 'persona.json'.")