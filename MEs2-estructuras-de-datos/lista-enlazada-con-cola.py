#*********Listas Enlazadas con 2 punteros claves 
class Nodo:
  def __init__(self,dato) -> None:
    #Datos que tienen la clase de Nodos
    self.dato=dato
    self.siguiente=None
    # Funcion extra no utilizada
  def valor(self):
    return f"este es el valor del nodo {self.dato} y esta es su dirrecion {self.siguiente}"

  #Funcion de la lista y donde se almacenan los nodos 
  
class Listaenlazada:
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
  def eliminar_dequeue(self):
    #Valor de la cola
    valor=self.cabeza.dato
    #Indico que cuando se guarde la cola solo avance un espacio a el otro nodo evitando un bucle 
    self.cabeza=self.cabeza.siguiente
    # Si apuntara a none pues no dirreciona a nada 
    if self.cabeza is None:
      self.cola=None

    # retorno el valor sacado 
    return f"Se ha sacado el primer valor el cual es: {valor}"

  ##########################################

  #Funcion que agrega un nodo a travez de la cola 
  def agregar_nodo_enqueue(self,dato):
    #El dato se estructura como un objeto Nodo 
    nuevo_nodo =Nodo(dato)
    #Comparación si existe algo en la lista 
    if self.esta_vacia() == True and self.cola_vacia() == True :
      self.cabeza = nuevo_nodo
      self.cola=nuevo_nodo
    else:
      #Si no hay nada entonce la cola se dirige al nuevo nodo
      self.cola.siguiente = nuevo_nodo
      #Se asigna que ahora la cola que antes apuntaba hacia cabeza apuntara a el nuevo nodo
      self.cola=nuevo_nodo

  def mostrar(self):
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
  def verfrente(self):
    if self.esta_vacia():
        return "La lista está vacía"
    return f"Su valor del frente es {self.cabeza.dato}"
  def vercola(self):
    if self.esta_vacia():
      return "La lista está vacía"
    return f"Su valor de la cola  es {self.cola.dato}"

clientes=Listaenlazada()

clientes.agregar_nodo_enqueue(7)
clientes.agregar_nodo_enqueue(9)
clientes.agregar_nodo_enqueue(11)
clientes.agregar_nodo_enqueue(1)
print(clientes.verfrente())
print(clientes.vercola())
print(clientes.mostrar())
clientes.eliminar_dequeue()
clientes.eliminar_dequeue()
print(clientes.mostrar())
clientes.agregar_nodo_enqueue(7)
print(clientes.mostrar())
clientes.eliminar_dequeue()
clientes.eliminar_dequeue()
clientes.eliminar_dequeue()
print(clientes.mostrar())
clientes.agregar_nodo_enqueue(9)
clientes.agregar_nodo_enqueue(15)
print(clientes.verfrente())
print(clientes.vercola())
print(clientes.mostrar())
clientes.eliminar_dequeue()
print(clientes.mostrar())


  

