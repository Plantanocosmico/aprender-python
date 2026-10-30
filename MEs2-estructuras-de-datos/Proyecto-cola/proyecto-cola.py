#Ejercicio banco con prioridad
#Importamos un numero ramdom 
import random


banner_banco=r"""
  _                           
 | |__   __ _ _ __   ___ ___  
 | '_ \ / _` | '_ \ / __/ _ \ 
 | |_) | (_| | | | | (_| (_) |
 |_.__/ \__,_|_| |_|\___\___/ 
                              
"""
# Clase prioritaria 
class FilaEnBanco:
  def __init__(self) -> None:
    self.lista=[]
    self.lista_ancianos=[]
    self.lista_deposito=[]
    self.lista_pagocheque=[]
    self.lista_pagotarjetacredito=[]

  def filavacia(self):
    if self.lista == []:
      return True
    return False
  
  def agregar(self,persona:dict):
    self.lista.append(persona)
    self.cantidad_elementos=None

  def mostrar(self):
    if self.filavacia()==True:
      "No existen elementos" 
    else:
      for observa_lista in self.lista:
        print(observa_lista)

  

  #ordeno las listas y pongo en otras listas  
  def ordenar(self):
    if self.filavacia() == True:
      return "No existen elementos por quitar en la lista: "
    else:
      adulto_mayor=60
      num=0
      for  num,valor in enumerate(self.lista):
        if valor["edad"] >= adulto_mayor:              #guardo item apra mostrar el item que he sacado 
          item=valor["edad"]
          self.lista_ancianos.append(item)
        elif valor["accion"] == "deposito":
          accion={valor["edad"],valor["accion"]}
          self.lista_deposito.append(accion)
        elif valor["accion"] == "pago de cheque":
          accion={valor["edad"],valor["accion"]}
          self.lista_pagocheque.append(accion)
        elif valor["accion"] == "pago de tarjeta de credito":
          accion={valor["edad"],valor["accion"]}
          self.lista_pagotarjetacredito.append(accion)
      r"""
      for  num,valor in enumerate(self.lista):
              if valor["edad"] >= adulto_mayor:
                #guardo item apra mostrar el item que he sacado 
                item=valor["edad"]
                lista_ancianos.append(item)
                #Saco el valor por particiones y se unen en la lista 
                self.lista[num:num+1]=[]
                
            return "Estos son ancianos: ",lista_ancianos
      
      """

  #Verifica que no haya ancianos 
  def no_hay_ancianos(self):
    if len(self.lista_ancianos) == 0:
      return True
    else:
      return False
  #Mostra a todos los ancianos 
  def mostrar_listadeancianos(self):
    if self.no_hay_ancianos() == True:
      return "No hay ancianos"
    else:
      return self.lista_ancianos
  
  def quitar_ancianos(self):
    if self.no_hay_ancianos() == True:
      return "Ya no hay ancianos"
    else:
      anciano_atendido=self.lista_ancianos[0]
      self.lista_ancianos.pop(0)
      return anciano_atendido 
  #***********TARJETAS***********
  #Verifica Pago de tarjeta de credito 
  def no_hay_pagos_tarjeta(self):
    if len(self.lista_pagotarjetacredito) == 0:
      return True
    else:
      return False
  #Mostra a todos los Pago de tarjeta de credito 
  def mostrar_listadepagostarjeta(self):
    if self.no_hay_pagos_tarjeta() == True:
      return "No hay clietes con tarjetas"
    else:
      return self.lista_pagotarjetacredito
    
  #Quitar pago de tarjeta

  def quitar_pagodetarjeta(self):
    if self.no_hay_pagos_tarjeta() == True:
      return "Ya no gente de pagos de tarjeta"
    else:
      cliente_tarjeta=self.lista_pagotarjetacredito[0]
      self.lista_pagotarjetacredito.pop(0)
      return cliente_tarjeta
    
  #***************DEPOSITO*********
  def no_hay_depositos(self):
    if len(self.lista_deposito) == 0:
      return True
    else:
      return False
  #Mostra a todos los Pagos de Deposito
  def mostrar_depositos(self):
    if self.no_hay_depositos() == True:
      return "No hay depositos"
    else:
      return self.lista_deposito

    
  def quitar_accion_de_depositar(self):
    if self.no_hay_depositos() == True:
       return "Ya no gente de depositos"
    else:
      cliente_deposito=self.lista_deposito[0]
      self.lista_deposito.pop(0)
      return cliente_deposito
    
  #*******************CHEQUE**********
  def no_hay_cheques(self):
      if len(self.lista_pagocheque) == 0:
        return True
      else:
        return False
  #Mostrar a todos los Pagos de Deposito
  def mostrar_cheques(self):
    if self.no_hay_cheques() == True:
      return "No hay depositos"
    else:
      return self.lista_pagocheque
      
  def quitar_accion_de_cheques(self):
      if self.no_hay_cheques() == True:
         return "Ya no gente de depositos"
      else:
        cliente_cheque=self.lista_pagocheque[0]
        self.lista_pagocheque.pop(0)
        return cliente_cheque
  


          
      
      






fila1=FilaEnBanco()
acciones=["deposito","pago de cheque","pago de tarjeta de credito"]
for i in range(15):
  persona={"edad":random.randint(18,90),"accion":random.choice(acciones) }
  fila1.agregar(persona)
print(banner_banco)
print("Bienvenido al banco")
print("Esta es la primera fila del banco")
print(fila1.mostrar())
print(fila1.ordenar())

print("Estos son los ancianos:",fila1.mostrar_listadeancianos())
while fila1.no_hay_ancianos() != True:
  print("Este es el anciano que se va:", fila1.quitar_ancianos())

print("Estos son los de tarjeta de credito:",fila1.mostrar_listadepagostarjeta())
while fila1.no_hay_pagos_tarjeta() != True:
  print("Este es el cliente de tarjeta que se va:", fila1.quitar_pagodetarjeta())

print("Estos son los de depositos:",fila1.mostrar_depositos())
while fila1.no_hay_depositos() != True:
  print("Este es el cliente de depositos que se va:", fila1.quitar_accion_de_depositar())


print("Estos son los de cheques:",fila1.mostrar_cheques())
while fila1.no_hay_cheques() != True:
  print("Este es el cliente de cheques que se va:", fila1.quitar_accion_de_cheques())

  


