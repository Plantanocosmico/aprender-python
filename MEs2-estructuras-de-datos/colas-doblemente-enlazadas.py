class NodoDoble:
  def __init__(self,dato) -> None:
    self.dato=dato
    #Este siguiente es el campo de uqe vien osea digamos [5] agregamso el [3] las litsa seria [3,5]
    self.siguiente=None
    #Este atras seria el contrario qeu esta atras [3,5] el atras seria el 5 
    self.atras=None


class ListaDoble:
  def __init__(self) -> None:
    #Se comprende cabeza que recorre desde el primer elmetno hasta el ultimo 
    #Se comprende cola desde el elmento ultimo hasta el primer elemento 
    self.cabeza=None
    self.cola=None


  def listadoblevacia(self):
    if self.cabeza == None:
      return True
    else:
      return False

  def agregar_al_frente(self,dato_nodo):
    nuevo_dato=NodoDoble(dato_nodo)
    if self.listadoblevacia() == True:
      self.cabeza=nuevo_dato
      self.cola=nuevo_dato
    else:
      #Este de aca seria la creacion del nuevo dato lo nasco y en su propiedad atras esta ya el 5 ponle
      nuevo_dato.atras=self.cabeza
      #En el campo de la cabeza siguientela anterior propiedad qeu exitia la nombro qeu su siguiente sera el nuevo nodo osea dle 5 el atras sera el siguiente
      self.cabeza.siguiente= nuevo_dato
      #Ahora el siguiente dato de la cabeza es el nuevo dato 
      self.cabeza=nuevo_dato

  def agregar_atras(self,dato_nodo):
    nuevo_dato=NodoDoble(dato_nodo)
    if self.listadoblevacia() == True:
      self.cabeza=nuevo_dato     
      self.cola=nuevo_dato
    else:
      nuevo_dato.siguiente=self.cola
      self.cola.atras=nuevo_dato
      self.cola=nuevo_dato
 #**************ELIMINA DATOS*********************
  def elimina_frente(self):
    if self.listadoblevacia() == True:
      self.cola=None
      self.cabeza=None
      return "No existen elementos para eliminar"
    else:
      if self.cabeza.atras == None:
        self.cabeza=None
        self.cola=None
        return "La lista Se ha vaciado "
      else:
        self.cabeza=self.cabeza.atras
        self.cabeza.siguiente=None

  def elimina_por_cola(self):
    if self.listadoblevacia() == True:
      self.cola= None
      self.cabeza=None
      return "No existen elementos para eliminar"
    else:
      if self.cola.siguiente == None:
        self.cabeza=None
        self.cola=None
        return "La lista Se ha vaciado "
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
#Prueba la lista si se borra correctamente de adelante 
assert liston.mostrar_lista_adelante() == [3,5,8,7]
print("Elimina la cola:")
liston.elimina_por_cola() 
print(liston.mostrar_lista_adelante())
#Prueba la lista si se borra correctamente de atras
assert liston.mostrar_lista_adelante() == [3,5,8]



#Esto es una prueba para saber si el esta correcto el uso de las propiedades con la propiedad  assert 
l = ListaDoble()
l.agregar_atras("A")
l.agregar_atras("B")
l.agregar_atras("C")
assert l.mostrar_lista_adelante() == ["A", "B", "C"]
assert l.mostrar_lista_atras() == ["C", "B", "A"]
print("Todo bien")


#En el caso que se borre todo el nodo por ambos lados se corrige con la correción del codigo 
lo = ListaDoble()
lo.agregar_atras("A")
lo.elimina_frente()
assert lo.mostrar_lista_adelante() == []
print(lo.mostrar_lista_adelante())
lo.agregar_atras("B")
lo.elimina_por_cola()
assert lo.mostrar_lista_atras() == []
