class Cola:
  def __init__(self) -> None:
    self.cola=[]
  def agregaralfinal(self,elemento:int):
    return self.cola.append(elemento)
  def sacardelfrente(self):
    if self.estavacia():
      return"La lista es vacia"
    return self.cola.pop(0)
  def estavacia(self):
    #da un booleano si existe o no 
    return len(self.cola) == 0
  def muestracola(self):
    if self.estavacia():
      return"La lista es vacia"
    print("Esta es la cola")
    return self.cola

print("Haremos una cola:")
c1=Cola()
c1.agregaralfinal(6)
c1.agregaralfinal(5)
c1.agregaralfinal(2)
print(c1.muestracola())
c1.sacardelfrente()
print(c1.muestracola())
c1.agregaralfinal(8)
c1.agregaralfinal(9)
print(c1.muestracola())
c1.sacardelfrente()
c1.sacardelfrente()
c1.sacardelfrente()
c1.sacardelfrente()
print(c1.sacardelfrente())