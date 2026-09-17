#importa json como ni idea 
import json
#crea un diccionario 
persona = {"nombre": "Leo", "edad": 22, "comida": "lasaña"}

#crea un archivo desde cero
 
with open("persona.json", "w", encoding="utf-8") as abre:
    json.dump(persona, abre, ensure_ascii=False, indent=4)

with open("persona.json", "r", encoding="utf-8") as f:
    datos = json.load(f)
    print(datos["nombre"])
    print(datos["edad"])