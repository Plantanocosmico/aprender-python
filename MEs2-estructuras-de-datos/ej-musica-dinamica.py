banner=r"""
 ____  _             _ _     _   
|  _ \| | __ _ _   _| (_)___| |_ 
| |_) | |/ _` | | | | | / __| __|
|  __/| | (_| | |_| | | \__ \ |_ 
|_|   |_|\__,_|\__, |_|_|___/\__|
               |___/             

"""
class Cancion:
  def __init__(self,valor:dict) -> None:
    self.valor=valor
    self.otracancion=None
  def mostrar(self):
    return "Este es el Nodo: ",self.valor

class Playlist:
  def __init__(self) -> None:
    self.ultimacancion=None
  def collecion_vacia(self):
    if self.ultimacancion == None:
      return True
    return False

  def agregarcanciones(self,cancion:dict):
    nueva_cancion=Cancion(cancion)
    if self.collecion_vacia() == True:
      self.ultimacancion = nueva_cancion
    else:
      revisa_cancion=self.ultimacancion
      while revisa_cancion.otracancion is not None:
        revisa_cancion = revisa_cancion.otracancion
      revisa_cancion.otracancion=nueva_cancion
  def mostrarcancion(self):
    lista_de_canciones=[]
    mostrar=self.ultimacancion
    ## Aqui definiria si ya no existen los objetos Cancion pues ya no hace el bucle
    while mostrar is not None:
      #En este caso nos importaria el dato que tiene no guardamos el enlace de meoria porque no lo necesitamos 
      lista_de_canciones.append(mostrar.valor) 
      mostrar=mostrar.otracancion
    return   lista_de_canciones
  def busqueda(self,nombre:str):
    listita=[]
    encontrado=True
    if self.collecion_vacia()== True:
      print("La collecion esta vacia ")
    else:
      
      punterobuscar=self.ultimacancion
      #Puse solo punterobuscar y no punterobuscar.otracancion ya que si ponemos este dato asi se originaria que el penultimo termino se slata la ver que el procimo sera null y no hara el codigo de decision mientra que si declaramos punterobuscar simplemente si existe o no existe buscara dentro de tods los nodos hasta que no tenga existencia 
      while punterobuscar is not None and encontrado==True:
        if punterobuscar.valor["cancion"]== nombre:
          encontrado=False
          return punterobuscar.valor
        punterobuscar = punterobuscar.otracancion 
      return "No existe ninguna cancion con ese nombre"
  def cantidad_de_canciones(self):
    contador_canciones=0
    punterocuenta=self.ultimacancion
    while punterocuenta is not None:
      contador_canciones += 1
      punterocuenta=punterocuenta.otracancion
    return contador_canciones
      

opcion=True
##****Creo mi objeto Playlist que almacenara mis canciones*********
coleccion_de_canciones=Playlist()
print(banner)
while opcion:
  print("¿Que deseas hacer? ")
  print("1.-Agregar cancion ")
  print("2.-Cantidad de Canciones ")
  print("3.-Buscar Cancion")
  print("4.-Salir")
  opciondeusuario=int(input("Escribe tu respuesta:"))
  if opciondeusuario == 1:
    print("Escribe los siguientes campos:")
    nombre_cancion=str(input("Escribe el nombre de la cancion: "))
    artista=str(input("Escribe el nombre del artista: "))
    año=int(input("Escribe el año de publicación: "))
    #**********Almaceno la respuestas dl usuario en la lista y en la funcion del metodo**********
    coleccion_de_canciones.agregarcanciones({"cancion":nombre_cancion,"autor":artista,"Publi":año})
    print("Canción añadida: ")
    print("*"*50)
    print("Estas es la lista de canciones: \n")
    for canciones in coleccion_de_canciones.mostrarcancion():
      print(canciones,"\n") 
  elif opciondeusuario ==2:
    print("La cantidad de canciones son:",coleccion_de_canciones.cantidad_de_canciones() )
  elif opciondeusuario ==3:
    #Esto claramente no tendria sentido si no hay un dato 
    if coleccion_de_canciones.collecion_vacia() == False:
      nombre=str(input("Escribe el nombre de la canción: "))
      print(coleccion_de_canciones.busqueda(nombre))
    else:
      print("No existe una playlist")
  elif opciondeusuario ==4:
      opcion = False