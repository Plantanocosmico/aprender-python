#**********Fases Proyecto********
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

def Cartelmenu() :
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
    nombretema=input("Escribe tu tema:")
    t1=Temas(nombretema)
    t1.crear

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
  def __init__(self,nombretema) -> None:
    self.nombretema=nombretema
  def crear(self):
    print("Imprimir mi tema ")
    #Aqui irira el with open en diferentes contexto 
  def eliminar(self):
    pass




#*******main o inicio*****************
print(bienvenida())

mantener=True
while mantener:
  print(Cartelmenu())
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
    print(verificar_opcion(opcion))
    mantener=opciones(opcion,mantener)
    













  

















