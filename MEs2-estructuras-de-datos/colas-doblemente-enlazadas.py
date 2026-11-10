class NodoDoble:
  def __init__(self,dato) -> None:
    self.dato=dato
    self.siguiente=None
    self.atras=None


class ListaDoble:
  def __init__(self) -> None:
    self.cabeza=None
    self.cola=None

  def listadoblevacia(self):
    if self.cabeza == None:
      return True
    else:
      return False

  def agregar_al_frente(self,dato_nodo):
    Nuevo_dato=NodoDoble(dato_nodo)
    if self.listadoblevacia() == True:
      self.cabeza=Nuevo_dato
      self.cola=Nuevo_dato
    else:
      Nuevo_dato.atras=self.cabeza
      self.cabeza.siguiente= Nuevo_dato
      self.cabeza=Nuevo_dato

  def agregar_atras(self,dato_nodo):
    Nuevo_dato=NodoDoble(dato_nodo)
    if self.listadoblevacia() == True:
      self.cabeza=Nuevo_dato     
      self.cola=Nuevo_dato
    else:
      Nuevo_dato.siguiente=self.cola
      self.cola.atras=Nuevo_dato
      self.cola=Nuevo_dato
 #**************ELIMINA DATOS*********************
  def elimina_frente(self):
    if self.listadoblevacia() == True:
      self.cola= None
      self.cabeza=None
      return "No existen elementos para eliminar"
    else:
      self.cabeza=self.cabeza.atras
      self.cabeza.siguiente=None

  def elimina_por_cola(self):
    if self.listadoblevacia() == True:
      self.cola= None
      self.cabeza=None
      return "No existen elementos para eliminar"
    else:
      self.cola=self.cola.siguiente
      self.cola.atras=None

  #************MUESTRAS LAS LISTAS*************
  def mostrar_lista_adelante(self):
    actual=self.cabeza
    lista=[]
    while actual is not None:
      lista.append(actual.dato)
      actual=actual.atras
    return lista

  def mostrar_lista_atras(self):
    actual=self.cola
    lista=[]
    while actual is not None:
      lista.append(actual.dato)
      actual=actual.siguiente
    return lista

liston=ListaDoble()
liston.agregar_al_frente(5)
liston.agregar_al_frente(3)
liston.agregar_al_frente(2)
liston.agregar_al_frente(9)
print(liston.mostrar_lista_adelante())
liston.agregar_atras(8)
liston.agregar_atras(7)
print("Esta es la diferencia entra la lista de adelante")
print(liston.mostrar_lista_adelante())
print("Esta es la diferencia entra la lista de atras")
print(liston.mostrar_lista_atras())
print("Elimina el frente de lo que hay ")
liston.elimina_frente()
liston.elimina_frente()
print(liston.mostrar_lista_adelante())
print("Elimina la cola:")
liston.elimina_por_cola()
print(liston.mostrar_lista_adelante())

