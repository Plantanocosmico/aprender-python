import json
#Tenga una lista de 3 personas con nombre, edad y comida favorita
#La guarde en un archivo personas.json
#La lea de vuelta
#Imprima solo las personas mayores de 18
#esta seria mi lista con 3 personas 
personas=[
  {"nombre":"Ana","edad":8,"comida":"gelatina"},
  {"nombre":"Mario","edad":26,"comida":"hamburguesas"},
  {"nombre":"Juan","edad":85,"comida":"queso"}
]
#esto tendria que guardar primero los datos a formatoo json o convertirlos 
with open("persona.json","w",encoding="utf-8") as abre:
  json.dump( personas, abre, ensure_ascii=False, indent=4)

with open("persona.json","r",encoding="utf-8") as recupera:
  datos=json.load(recupera)
  edades=[]
  for edades in datos:
    if edades["edad"] >= 18:
      print(f"{edades["nombre"]} es {edades["edad"]}")
    else: 
      print("no eres mayor")

  

  #print(f"{datos["nombre"]} es mayor de edad {datos["edad"]} ")



