#En general creamos una lista para que los tipos deban ser de esta clase en si srive como un int,string,float,list,ect entonces nuestro valor se vuelve como un pilita en este caso 
#lista=Pilitas es igula a lista:Pilitas

class Pilitas :
  #Indica la lista vacia para todos los elementos de este tipo 
  def __init__(self) -> None:
    lista=[]
    self.lista=lista
  #Ayuda del chat si esta vacia 
  def esta_vacia(self):
    return len(self.lista) == 0
  #Define sus metodos o buenos los defino en esta parte con push ver todo y vertope tambien quitar 
  def push(self,elemento):
    #agrega un elemtno a el objeto 
    self.lista.append(elemento)
  def vertodo(self):
    if len(self.lista) == 0:
      return "La lista esta vacia"
    #en el campo para mostrar toda la lista 
    return self.lista
  def vertope(self):
    #ve el tope 
    return self.lista[-1]
  def pop(self):
    if len(self.lista) == 0:
     return "La lista esta vacia"
    #elimina el primer elemetno que ve al final 
    return self.lista.pop(-1)

#Metodo arcaico xd 
print("Pilas")
p1=Pilitas()
p1.push(4)
p1.push(6)
p1.push(10)
print(p1.vertodo())
print(p1.vertope())
p1.pop()
print(p1.vertodo())
p1.pop()
p1.pop()
print(p1.pop())



