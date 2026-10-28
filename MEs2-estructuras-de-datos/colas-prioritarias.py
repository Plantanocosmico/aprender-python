#***********COLAS PRIORITARIAS********************
#En las colas prioritarias podemos ver las caracteristicas de un cola normla asi que definimos una cola nomral con una cabeza y cola 
class Nodo:
  def __init__(self,dato) -> None:
    self.dato=dato
    self.siguiente=None
class ListaColaPrioritaria:
  def __init__(self) -> None:
    self.prioridad=None
    self.cabeza=None
    self.cola=None
  def estavacio(self):
    if self.cabeza == None:
      return True
    return False
  def agregarelemento(self,valor):
    nuevo_nodo=Nodo(valor)
    if self.estavacio() == True:
      self.cabeza=nuevo_nodo
      self.cola=nuevo_nodo
      self.prioridad=nuevo_nodo
    else:
      self.cola.siguiente=nuevo_nodo
      self.cola=nuevo_nodo

  def mostrar(self):
    actual=self.cabeza
    listaprioridad=[]
    while actual is not None:
      listaprioridad.append(actual.dato)
      actual=actual.siguiente
    return listaprioridad

  def sacar(self):
    if self.estavacio() == True:
      self.cabeza=None
      self.cola=None
      return "No hay elemento en la cola"
    else:
      self.cabeza=self.cabeza.siguiente


hospital=ListaColaPrioritaria()
hospital.agregarelemento(4)
hospital.agregarelemento(6)
hospital.agregarelemento(7)
print("Esta es la lista: ",hospital.mostrar())
hospital.sacar()
print("Esta es la lista: ",hospital.mostrar())
hospital.agregarelemento(1)
print("Esta es la lista: ",hospital.mostrar())

#Cola Prioritaria
class ColaPrioritaria():
  def __init__(self) -> None:
    self.lista=[]
  def estavacia(self):
    if self.lista == []:
      return True
    return False
  
  def agregar(self,dato):
    self.lista.append(dato)

  def quitar(self):
    if self.estavacia() == True:
      return "La lista esta vacia"
    else:
      prioritario=0
      for num in range(1,len(self.lista)):
        #mido los componentes de lla lista 1 por 1 
        if self.lista[num] > self.lista[prioritario]:
          prioritario=num
      #guardo item apra mostra el item que he sacado 
      item=self.lista[prioritario]
      #Saco el valor por particiones y se unen en la lista 
      self.lista[prioritario:prioritario+1]=[]
      #retorno el item dado 
      return item
  def mostrar(self):
    return self.lista

urgencias=ColaPrioritaria()
urgencias.agregar(15)
urgencias.agregar(1)
urgencias.agregar(78)
print("Estos son los elementos en la lista: \n", urgencias.mostrar())
while urgencias.estavacia() == False:
  print("De repente hubo un problema el primero en ser atendido es:", urgencias.quitar())



