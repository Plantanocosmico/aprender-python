class Animal:
  def __init__(self, nombre: str, edad: int) -> None:
    self.nombre=nombre
    self.edad=edad

  def descripcion(self)-> str:
    return f"Es un {self.nombre} y tiene {self.edad}"
class Perro(Animal):
  def __init__(self, nombre: str, edad: int,raza:str) -> None:
    super().__init__(nombre, edad)
    self.raza=raza

  def ladra(self):
    if self.edad > 5:
      return f"El perro:{self.nombre} esta ladrando"
    else:
      return f"El pero es un bebe \n Su edad es:{self.edad}"

animales=Animal("Piki",12)
miperro=Perro("Chiki",6,"Hoski")
print(f"mi perro {miperro.descripcion()} \ny esta {miperro.ladra()}")
