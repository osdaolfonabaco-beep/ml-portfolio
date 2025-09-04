import json
data = {
    "nombre": "Manzana", 
    "precio": 1.5,
    "cantidad": 2

}

with open("datos_ejemplo.json", "w") as archivo:
    json.dump(data, archivo, indent = 4)

print("Datos guardados en 'datos_ejemplo.json'")

with open("datos_ejemplo.json", "r") as archivo:
    datos_cargados = json.load(archivo)

print("Datos cargados desde archivo: ")
print(datos_cargados)

