banner_banco=r"""
  ____                        
 | __ )  __ _ _ __   ___ ___  
 |  _ \ / _` | '_ \ / __/ _ \ 
 | |_) | (_| | | | | (_| (_) |
 |____/ \__,_|_| |_|\___\___/ 
                              
"""
#*********Listas Enlazadas con 2 punteros claves 
class Cliente:
  def __init__(self,dato:dict) -> None:
    #Datos que tienen la clase de Nodos
    self.dato=dato
    self.siguiente=None
    # Funcion extra no utilizada
  def valor(self):
    return f"este es el valor del nodo {self.dato} y esta es su dirrecion {self.siguiente}"

  #Funcion de la lista y donde se almacenan los nodos 
  
class Listadeclientes:
  #Defino los punteros iniciales de cola y cabeza 
  def __init__(self) -> None:
    #Punteros claves de donde ponen los datos y donde sacan los nodos 
    self.cabeza=None
    self.cola=None
  #Funcion en detalle si la cola esta vacia 
  def esta_vacia(self):
    if self.cabeza == None:
      return True
    return False
  #Funcion de la cola si esta vacia 
  def cola_vacia(self):
    if self.cola == None:
      return True
    return False
  #funcion que elimina la cabeza de la lista o el primero en entrar es el primero en salir Simulando una estructura FIFO de la cola 
  def eliminar_cliente(self):
    #Valor de la cola
    valor=self.cabeza.dato
    #Indico que cuando se guarde la cola solo avance un espacio a el otro nodo evitando un bucle 
    self.cabeza=self.cabeza.siguiente
    # Si apuntara a none pues no dirreciona a nada 
    if self.cabeza is None:
      self.cola=None

    # retorno el valor sacado 
    return f"Se ha atendido al primer cliente : {valor}"

  ##########################################

  #Funcion que agrega un nodo a travez de la cola 
  def agregar_cliente_enqueue(self,dato):
    #El dato se estructura como un objeto Nodo 
    nuevo_cliente =Cliente(dato)
    #Comparación si existe algo en la lista 
    if self.esta_vacia() == True and self.cola_vacia() == True :
      self.cabeza = nuevo_cliente
      self.cola=nuevo_cliente
    else:
      #Si no hay nada entonces la cola se dirige al nuevo nodo
      self.cola.siguiente = nuevo_cliente
      #Se asigna que ahora la cola que antes apuntaba hacia cabeza apuntara a el nuevo nodo
      self.cola=nuevo_cliente

  def mostrar_lista_de_clientes(self):
    #una variable creada para analizar las estructuras iguales de nodos 

    actual=self.cabeza
    #una lista donde se posicionan los nodos
    lista=[]

    #Aun hay un bucle para mostrar todos los nodos ya que tenemos que recorrer t0odos y se vuelve una función O(n) 
    while actual is not None:
      lista.append(actual.dato)
      actual=actual.siguiente
    return lista
  
  #Ver valores sin sacarlos 
  def primer_cliente_enfila(self):
    if self.esta_vacia():
        return "No hay clientes"
    return f"El cliente mas cercano es  {self.cabeza.dato}"
  def utlimo_cliente_enfila(self):
    if self.esta_vacia():
      return "No hay clientes"
    return f"El cliente mas lejano es  {self.cola.dato}"



opcion=True
##****Repollo del anterior codigo*********
banco=Listadeclientes()
banco.agregar_cliente_enqueue({"nombre":"Juan","ticket":1})
banco.agregar_cliente_enqueue({"nombre":"Maria","ticket":2})
banco.agregar_cliente_enqueue({"nombre":"Lucas","ticket":3})


print(banner_banco)
while opcion:

  print("Hola tenemos bastantes clientes hoy.... ")

  print("¿Que deseas hacer? ")
  print("1.-Llega cliente nuevo ")
  print("2.-Atender cliente ")
  print("3.-Quien es el siguiente cliente? ")
  print("4.-Quienes clientes esperan: ")
  print("5.-Salir ")
  opciondeusuario=int(input("Escribe el numero de que quieres hacer:"))

  if opciondeusuario == 1:
    print("Escribe los siguientes campos:")

    nombre=str(input("Escribe el nombre del cliente: "))

    ticket=int(input("Escribe el ticekt del cliente: "))
    #**********Almaceno la respuestas del usuario en la lista y en la funcion del metodo**********
    banco.agregar_cliente_enqueue({"nombre":nombre,"ticket":ticket})
    print("Cliente añadido:")
    print("*"*50)
   
  elif opciondeusuario ==2:
    print(banco.eliminar_cliente())
  elif opciondeusuario ==3:
    print(banco.primer_cliente_enfila())
  elif opciondeusuario ==4:
    print("Estos son los clientes actuales:")
    for recorre in banco.mostrar_lista_de_clientes():
      print (recorre["ticket"],recorre["nombre"])


  elif opciondeusuario == 5:
    opcion=False