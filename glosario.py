# malos.append() agrega un elemento al final de una lista vacía
# En si al final de la cola 
# tuplas (El concepto trata de devolver 2 valores a la vez )lista inmutbale sin cambio alguno 
# Un archivo es un conjunto de datos guardados en el disco duro de tu computadora.

#"w" Sirve para borrar desde cero comienza  con lo anterior  
#"r" solo lee 
#"a" Agrega a lo que ya estaba 
##para archivos ##
#f.read() Sirve  para leer los archivos del texto 
#f.write() Sirve para escribir palabras 
#f.strip() elimina espacios y saltos de línea al inicio y final de un texto.

########## JSON ##############
#ensure-ascii "permite caracteres especiales como ñ y tildes en prpiedad false"
#indent Define cuántos espacios de sangría tiene el JSON.
#dump vacia tu diccionario Python y lo convierte a formato JSON dentro del archivo
#load() Lee el archivo JSON y lo convierte de vuelta a diccionario Python para que puedas usar datos["nombre"] normalmente. supongo para leer el diccionario y poder isar esos datos en un diccionario como variables



########## CLASS ##############

#class — define el molde de atributos y metodos 
#__init__ — se ejecuta automáticamente al crear el objeto, guarda los datos 
# Prepara l objeto con sus datos iniciales tambein concido como constructor  
#self — es el objeto mismo, como decir "yo"
#pass — es un placeholder, le dice a Python "aquí habrá código después, por ahora no hagas nada". Útil cuando defines métodos vacíos.

####type hints son como etiquetas que le ponen tipo a variables y funciones:
#como digamos cada variable tendria que dar algo 
#Ejemplo 
## Sin type hints
#def sumar(a, b):
  #  return a + b

# Con type hints
#def sumar(a: int, b: int) -> int:
 #   return a + b
#

#Callable[..., dict]: Explica que lo que hay dentro de la lista es algo que se puede "llamar" o ejecutar (como una función o método). Los puntos suspensivos ... significan que la función puede recibir cualquier tipo de argumento, y la palabra dict significa que, al final, te devolverá un diccionario.

#estudiar list comprehension

#####HERENCIA#####
 #class Perro(Animal) — Perro hereda todo de Animal
 # super().__init__(nombre, edad) llama al __init__ del padre para no repetir código