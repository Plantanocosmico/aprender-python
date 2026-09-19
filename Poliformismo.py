class Animal:
  def __init__(self, nombre: str, edad: int) -> None:
    self.nombre=nombre
    self.edad=edad

  def descripcion(self)-> str:
    return f"Es un {self.nombre} y tiene {self.edad}"
class Pajaro(Animal):
  def __init__(self, nombre: str, edad: int, alas: bool) -> None:
    super().__init__(nombre, edad)
    self.alas=alas
  def volar(self):
    if self.alas == True:
      return f"El pajaro {self.nombre} esta volando"
    else:
      return f"El pajaro {self.nombre} no puede volar"
  def sonido(self):
    if self.edad > 3:
      return f"El pajaro:{self.nombre} esta cantando "
    else:
      return f"El pajaro es un bebe \n Su edad es:{self.edad}"


class Gato(Animal):
  def __init__(self, nombre: str, edad: int, raza:str ) -> None:  
    super().__init__(nombre, edad)
    self.raza=raza
  def sonido(self) -> str:
    if self.edad > 3:
      return f"El gato:{self.nombre} esta maullando "
    else:
      return f"El gato es un bebe \n Su edad es:{self.edad}"
    
class Perro(Animal):
  def __init__(self, nombre: str, edad: int,raza:str) -> None:
    super().__init__(nombre, edad)
    self.raza=raza

  def sonido(self):
    if self.edad > 5:
      return f"El perro:{self.nombre} esta ladrando"
    else:
      return f"El pero es un bebe \n Su edad es:{self.edad}"
miperro=Perro("Chiki",6,"Hoski")
migato=Gato("michu",5,"africano")
mipajaro=Pajaro("Yino",5,True)

animales=[miperro,migato,mipajaro]
for animal in animales:
  print(f"{animal.sonido()}")
print("")



print(f"Mi perro: {miperro.descripcion()} \n{miperro.sonido()}")
print("")
print(f"Mi gato: {migato.descripcion()} \n{migato.sonido()}")
print("")
print(f"Mi pajaro: {mipajaro.descripcion()} \n{mipajaro.sonido()}\n{mipajaro.volar()}")
