#Un ejemplo de archivo es lo siguiente 
#w borra lo anterior para recrearlo desde cero 

#with open("lista-super.txt","w",encoding="utf-8") as lista:
#  lista.write("Manzanas \n")
#  lista.write("Bananas \n")
#  lista.write("Peras \n")

#print(f"Esta es la lista de alimentos {lista}")

def crear(archivo,n,c):
  datos=f"hola soy {n},mi comida favorita es{c}"
  with open(f"{archivo}.txt","w",encoding="utf-8")as adjunto:
    adjunto.write(datos)
    return datos
  
def leer(archivo):
  with open(f"{archivo}.txt","r", encoding="utf-8") as ver:
    contenido: str =ver.read()
    return contenido
  
def agregar(archivo,n,c):
  sumar =f"mi nombre es {n} mi comida favorita es {c} \n"
  with open(f"{archivo}.txt","a",encoding="utf-8") as agre:
    agre.write(sumar)
        
def leerlinea(archivo):
  with open(f"{archivo}.txt", "r", encoding="utf-8") as leerlinea:
    for linea in leerlinea:
        print(linea.strip())

#Ejercicio 
narchivo=input("Como se llamara el archivo: ")
nombre="juan"
comida="lasaña"
leerlinea(narchivo)
