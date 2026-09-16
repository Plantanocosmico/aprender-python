#Un ejemplo de archivo es lo siguiente 
#w borra lo anterior para recrearlo desde cero 




with open("lista-super.txt","w",encoding="utf-8") as lista:
  lista.write("Manzanas \n")
  lista.write("Bananas \n")
  lista.write("Peras \n")

print(f"Esta es la lista de alimentos {lista}")

def crear(archivo,n,c):
  datos=f"hola soy {n},mi comida favorita es{c}"
  with open(f"{archivo}.txt","w")as adjunto:
    adjunto.write(datos)
    return datos

#Ejercicio 
narchivo=input("Como se llamara el archivo: ")
nombre="juan"
comida="lasaña"
crear(narchivo,nombre,comida)
