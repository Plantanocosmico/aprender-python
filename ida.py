#Primero veremos las variables para que sirve cada uno 
#Un dato como int pero con capacidad e mostrar decimales o datos enteros 
x = 20


#un strign de palabras 
nombre="Sandia"
#Un booleano  con capacidade de true o false 
aprobado= False
#En este caso mostramos las variables pero sin ninguna muestra o algo 
#ahora para imprimir los datos o mostralos en la consola podemos utilizar el comando print 
print(x)
print(nombre)
print(aprobado)
#Esto imprime los datos recopilados en lo que guardamos antes en los espacio de la memoria ram y los muestra 
#ahora aparte de esos datos veremos que tipo son
print("")
print(type(x)) #ocupa 28 bytes 
print(type(nombre))
print(type(aprobado))

#Ahora veremos un diccionario 
person =[()] #Esto seria una lista que contiene una tupla

persona=[] # Esto es una lista 

peronas={} #Esto es un diccionario 


#¿Que hace cada uno?

#el Any significa datos de cualquier tipo 
#el dict es un diccionario que almacena en formato clave y valor 
iguales={"nombre":"Ana","b": 50 ,"1":True }
print("")
print(iguales)
print("Aqui vemos el valor de cada uno separado:")
print(iguales["1"])
print(iguales["b"])
print(iguales["nombre"])
print("")
print("Y aqui vemos que tipos son:")
print(type(iguales["nombre"]))
print(type(iguales["b"]))
print(type(iguales["1"]))

#Ese es un dicicionario con varios datos 

#ahora veremos el otro set de valores unicos que tambien se contaria como diccionario 
print("")
personas={"casa":"barro","apellido":"paco","comida":"sandia" }
#El set indica que cada campo es una coleecion sin repetirse 
colores = {"rojo", "azul", "verde"}
#el str significa todos los campos deben o empiezan siendo strig
dinero=20
print(f"Bueno en si veremos a {personas['apellido']} el tiene una casa de {personas["casa"]} y su comida favortia es la {personas['comida']} y no olvidar que gana {dinero} ")

edad =-15
if edad >= 18:
  print("Eres mayor de edad")
elif edad >=0 and edad <= 17: #Rn este caso soloo veo el cambio de en vez de else es elif para los cambios o como escaleras y para la condicon final sigue siendo else 
  print("No eres mayor de edad")
else:
  print("Creo que no escribiste tu edad xd o eres muy viejo ")