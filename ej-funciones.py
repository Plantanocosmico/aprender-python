#Accion de la función
mouse={"nombre": "mesa","precio":20,"estado":"malo" }
compu={"nombre": "compu","precio":2000,"estado":"bueno" }
telefono={"nombre": "telefono","precio":4420,"estado":"malo" }
objetos=[mouse,compu,telefono]

#iria la lista para recoger 
def saber(lista):
  objetos1=[]
  objetos2=[]
  for recoger in lista:
    if recoger["estado"] == "malo":
      objetos1.append(recoger["nombre"])
    elif recoger["estado"]== "bueno":
      objetos2.append(recoger["nombre"])
    else:
      print("nose")
  return objetos1,objetos2,

malos, buenos = saber(objetos)
print(f"Malos: {malos}")
print(f"Buenos: {buenos}")

casa=saber(objetos)
print("\n")
print(f"Esto deberia imprimir todos mis objetos : {casa}")

