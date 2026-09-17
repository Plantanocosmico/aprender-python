import json


class Persona:
    def __init__(self, nombre, edad,):
        self.nombre = nombre
        self.edad = edad
        # El self.nombre hace que el objeto perdure a lolargo del tiempo
    def saludar(self):
        return f"Hola soy {self.nombre} y tengo {self.edad} años"

juan = Persona("Juan", 22)
print(juan.saludar())




class Productos:
  #Una clase de compone de atributo y metodos aqui se ponen los atributos: 
  def __init__(self,nombre,precio,descripcion) -> None:
    self.nombre=nombre #Acepta cualqueir valor 
    self.precio=precio
    self.descripcion=descripcion
  #Aca se definirian los metodos del atriibuto o las acciones 
  def correr(self):
    pass
  def nombrar(self):
    return f"Producto agregado: {self.nombre}\n {self.precio} \n {self.descripcion}"
  def a_diccionario(self) -> dict:
    return {
        "nombre": self.nombre,
        "precio": self.precio,
        "descripcion": self.descripcion
    }

p1=Productos("crema",55,"Sirve para todo el cuerpo")
p2=Productos("Bloqueador",35,"Sirve para la cara")
p3=Productos("Depiladora",15,"Sirve para todo el cuerpo")
lista= [p1,p2,p3]

datos = []
for produc in lista:
  elementos =produc.a_diccionario()
  datos.append(elementos)
with open("clases-json.json","w",encoding="utf-8")as guardaelementos:
   json.dump(datos,guardaelementos,ensure_ascii=False,indent=4) 

  
  

   



