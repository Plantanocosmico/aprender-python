
class NodoPersonas:
  def __init__(self,dato) -> None:
    self.dato=dato
    self.siguiente=None

class JuegodeRol:
  def __init__(self) -> None:
    self.cabeza=None
    self.cola=None
  def estavacio(self):
    if self.cabeza == None:
      return True
    return False
  def agregarpersona(self,persona):
    nueva_persona=NodoPersonas(persona)
    if self.estavacio() == True:
      self.cabeza=nueva_persona
      self.cola=nueva_persona
      nueva_persona.siguiente=nueva_persona
    else:
      #eso cambia la dirrecion de siguiente a un nodo nuevo
      self.cola.siguiente=nueva_persona
      #Esto apunta la propiedad del nuevo nodo siguiente a la cabeza 
      nueva_persona.siguiente=self.cabeza
      #Esto apunta que la cola se cambiara sus valores por el nuevo nodo 
      self.cola=nueva_persona

  def mostrar(self,pasos=10):
    actual = self.cabeza
    contador=0
    print("Cola circular....")
    while actual and contador<pasos:
      print(actual.dato, end="->")
      actual=actual.siguiente
      contador += 1

  def eliminar_frente(self):
    if self.estavacio() == True:
      return "No existen elementos que eliminar"
    else:
      self.cabeza=self.cabeza.siguiente
      self.cola.siguiente=self.cabeza

  def eliminar_cola(self):
      apuntador=self.cabeza
      if self.estavacio() == True:
        return "No existen elementos que eliminar"
      else:
        while apuntador.siguiente != self.cola:
          apuntador=apuntador.siguiente
        self.cola=apuntador
        self.cola.siguiente=self.cabeza
    
lc=JuegodeRol()
lc.agregarpersona(5)
lc.agregarpersona(6)
lc.agregarpersona(7)
print(lc.mostrar())
lc.eliminar_frente()
print(lc.mostrar())
lc.agregarpersona(9)
lc.agregarpersona(1)
print(lc.mostrar())
lc.eliminar_cola()
lc.eliminar_cola()
print(lc.mostrar())

    