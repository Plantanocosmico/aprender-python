#**********Fases Proyecto********
#****IMPORT****
import json
import os 
from datetime import datetime


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

  def crearTema(self):
    #Evaluamos si existe primero un archivo guardado como esa variable 
    try:
      with open("arcreados.json","r",encoding="utf-8")as revisa:
        contenido=json.load(revisa)
    except FileNotFoundError:
      #Se crea la lista para poner las tareas  soloo una vez cuando se haya creado la carpeta
      contenido=[]    
      #En este caso almacena la traida del usario en tareas y lo deposita en colleciondetareas en su cola

    #Echo por el chat en si que pasaria si en el archivo json esgta vacio esa no me la vi venir 
    except json.JSONDecodeError:
      contenido = [] 


    #Pide el nombre del archivo y la fecha actual primero saca los datos y luego con la funcion strftime saca la fecha 
    fecha=datetime.now().strftime("%d/%m/%Y %H:%M")
    tareas={"Archivo":self.nombrearchivo,"Fecha":fecha}
    contenido.append(tareas)
    #Creamos el archivo ahora si 
    with open("arcreados.json","w",encoding="utf-8") as abre:
      json.dump(contenido,abre, ensure_ascii=False, indent=4)

    #Vovemos a ponerle una descripcion al archivo en este caso para su creación
    descripcion=str(input("Descripcion rapida:"))
    #Pondremos una ruta para todas las notas en este caso como es una version de pracvtica solo en una carpeta 
    ruta=f"notas/{self.nombrearchivo}.txt"
    #***********NUEVO************
    #****Creacion de carpeta*******
    os.makedirs("notas",exist_ok=True)
    #Como la ruta tiene al archivo guardamos en ruta 
    with open(ruta,"w",encoding="utf-8") as contenido:
      contenido.write(descripcion)
      print("Tu archivo fue creado con exito:")

      #Verificacion si el archivo existe 
      try:
        #Nuevo
              #abre el archivo conviertiendole en una ruta absoluta 
        rutaabsoluta=os.path.abspath(ruta)
        os.startfile(rutaabsoluta)
      except FileNotFoundError as nocrear:
        print(f"Se producio un error {nocrear}")  
      return descripcion
    
  
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
    


