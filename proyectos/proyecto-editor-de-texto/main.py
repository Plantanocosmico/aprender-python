#**********Fases Proyecto********
#****IMPORT****
import json



#Fase 1.1 Interfaz de app
def bienvenida() -> str:
  nombre=input("Como te llamas? ")
  letrero = r"""
  ********************************************
  _   _      _ _         _               
  | | | |    | | |       | |              
  | |_| | ___| | | ___   | |__  _ __ ___  
  |  _  |/ _ \ | |/ _ \  | '_ \| '__/ _ \ 
  | | | |  __/ | | (_) | | |_) | | | (_) |
  \_| |_/\___|_|_|\___/  |_.__/|_|  \___/ 
                                          
  ********************************************                                                        
  """
  saludo=f"Bienvenido {nombre}!!!!! ☺ "
  inicio=f"{letrero}  {saludo} "
  return inicio

#Cartel del menu 

def cartel_menu() :
  menu =r"""
  ************************************************************************************
     __        ___     __          ___  __   ___  __                __   ___  __  __ 
    /  \ |  | |__     /  \ |  | | |__  |__) |__  /__`    |__|  /\  /  ` |__  |__)  _|
    \__X \__/ |___    \__X \__/ | |___ |  \ |___ .__/    |  | /~~\ \__, |___ |  \  . 
    
  ************************************************************************************                                                                                             
    """
  return menu


def opciones(eleccion,mantener:bool):
  if eleccion == 0:
    mantener = False
  if eleccion == 1:
    nombrearc=input("Escribe tu tema:")
    t1=Temas(nombrearc)
    t1.crearTema()

  if eleccion == 2:
    pass
  return mantener

#**************Verifica si la opcion esta bien*************************** 
def verificar_opcion(eleccion):
  if eleccion <0:
    raise ValueError("Escribe un numero valido:")
  return f"Entrando a opcion: {eleccion}......"
  

#**********Clase Tema********************
class Temas():
  def __init__(self,nombrearchivo) -> None:
    self.nombrearchivo=nombrearchivo

  def crearJson(self):
    pass

  def crearTema(self):
    creadojson=False
    tareas={"Archivo":f"{self.nombrearchivo}"}
    colleciondetareas=[tareas]
    if creadojson == False:
      with open("arcreados.json","w",encoding="utf-8") as abre:
        json.dump(tareas,abre, ensure_ascii=False, indent=4)
        creadojson = True
    if creadojson == True:
      descripcion=str(input("Descripcion rapida:"))
      with open(f"{self.nombrearchivo}.txt","w",encoding="utf-8") as contenido:
        contenido.write(descripcion)
        print("Tu archivo fue creado con exito:")
        return descripcion
    
    #Aqui iria el with open en diferentes contexto 
  def eliminar(self):
    pass




#*******main o inicio*****************
print(bienvenida())

mantener=True
while mantener:
  print(cartel_menu())
  print("*"*50)
  print("""
    Opciones:
    0.-Salir 
    1.-Crear
    2.-Eliminar
    """)
  print("*"*50)
  try:
    opcion=int(input("Escribe el numero de la opcion que quieras realizar:"))
    verificar_opcion(opcion)
  except TypeError as error:
    print(f"Tienes un error:{error}") 
  except ValueError as error:
    print(f"Se encontro un error:{error}")
  else:
    mantener=opciones(opcion,mantener)
    













  

















