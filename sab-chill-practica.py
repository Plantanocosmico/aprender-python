mouse={"nombre": "mesa","precio":20,"estado":"malo" }
compu={"nombre": "compu","precio":2000,"estado":",bueno" }
telefono={"nombre": "telefono","precio":4420,"estado":"malo" }
objetos=[mouse,compu,telefono]
for rec in objetos:
  sandia=rec["estado"]
  if sandia == "malo":
    print(f"Este objeto {rec["nombre"]} esta {sandia}")
print("\n")
print(f"{objetos[0]},\n{objetos[1]},\n{objetos[2]}")
print(f"Total de objetos: {len(objetos)}")
#Len permite contar elemtnos de una lista determinada