class Producto:
  def __init__(self,nombre:str,precio:int) -> None:
    if precio < 0:
      raise ValueError("El precio debe ser positivo")
    if nombre == "":
      raise ValueError("El producto debe tener un nombre")
    self.nombre=nombre
    self.precio=precio
    
  def llamar(self):
    return f"El producto es {self.nombre} con precio:{self.precio}"


try:
  p1=Producto("Vaselina",-5)
  print(f"{p1.llamar()}")
except ValueError as error:
  print( f"El error es:{error}")

try:
  p2=Producto("", 4)
  print(f"{p2.llamar()}")
except ValueError as error:
  print( f"El error es:{error}")

try:
  p3=Producto("Bloqueador", 8)
  print(f"{p3.llamar()}")
except ValueError as error:
  print( f"El error es:{error}")