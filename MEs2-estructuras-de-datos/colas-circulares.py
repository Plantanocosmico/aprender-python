class Personas:
  def __init__(self,dato) -> None:
    self.dato=dato
    self.siguiente=None

class Juego:
  def __init__(self) -> None:
    self.cabeza=None
    self.cola=None
  def esta_vacia(self):
    if self.cabeza == None:
      return True
    return False
  def agregar_jugador(self,dato):
    nuevo_jugador=Personas(dato)
    if self.esta_vacia() == True:
      self.cabeza=nuevo_jugador
      self.cola=nuevo_jugador
      nuevo_jugador.siguiente=nuevo_jugador
    else:
      self.cola.siguiente = nuevo_jugador
      nuevo_jugador.siguiente=self.cabeza
      self.cola=nuevo_jugador
      
  def mostrar(self):
    actual =self.cabeza
    lista_jugadores=[]
    while actual.siguiente != self.cabeza:
      lista_jugadores.append(actual.dato)
      actual=actual.siguiente
    lista_jugadores.append(actual.dato)
    return lista_jugadores
futbol=Juego()
futbol.agregar_jugador(3)
futbol.agregar_jugador(4)
futbol.agregar_jugador(5)
print(futbol.mostrar())


