"""
class Siguiente:
  def __init__(self,numero ) -> None:
    self.numero=numero
  def supongamos(self):
    return self.numero
  

class Nodo:
  def __init__(self,) -> None:
    self.siguiente=papa.numero
  def valor(self,valor):
    return f"este es el valor del nodo {valor} y esta es su dirrecion {self.siguiente}"
dirrecionamiento=4
papa=Siguiente(dirrecionamiento)
n1=Nodo()
print(n1.valor(6))


cliente=Nodo(6)
print(cliente.valor())
listama=Listaenlazada()
print(listama.esta_vacia())
"""
class Nodo:
  def __init__(self,dato) -> None:
    self.dato=dato
    self.siguiente=None
  def valor(self):
    return f"este es el valor del nodo {self.dato} y esta es su dirrecion {self.siguiente}"
class Listaenlazada:

  def __init__(self) -> None:
    self.cabeza=None

  def esta_vacia(self):
    if self.cabeza == None:
      return True
    return False
  def agregar_nodo(self,dato):
    nuevo_nodo =Nodo(dato)
    if self.esta_vacia() == True:
      self.cabeza = nuevo_nodo
      
    else:
      actual =self.cabeza 
      while actual.siguiente is not None:
        actual = actual.siguiente
      actual.siguiente=nuevo_nodo
  def mostrar(self):
    actual=self.cabeza
    lista=[]
    while actual is not None:
      lista.append(actual.dato)
      actual=actual.siguiente
    return lista

clientes=Listaenlazada()

clientes.agregar_nodo(7)
clientes.agregar_nodo(9)
clientes.agregar_nodo(11)

print(clientes.mostrar())


  

