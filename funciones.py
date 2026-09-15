def saludar(nombre):
  print(f"Hola we {nombre}")

saludar("Juan")
saludar("Marcos")
print(f"{saludar("jiuan")}") #En este caso no funcona porque la funcion por si misma devuleve nada osea solo hace la actividad que hemos hecho anteriormente para que la funcion de un resultado tenemos que configurarla

def sumar(a, b):
  return a + b

resultado = sumar(10, 5)
print(resultado)

print("\n")



#Este pedazo de codigo esta bien pero me menciona que el error esta en como el print al enviar una cadena de texto no mantiene ninguna valos para enviar en la fucnción es por ello que el codigo aparecera en node 
def participacion(edad,apellido):
  if edad >= 5 and edad <= 20 :
    print("Edad permitida")
    print(f"Puedes ingresas {apellido}")
    return (print(f"Estas admitido con tu año:{edad}, {apellido}"))
  else:
    return (print("No eres admitido"))

participacion(50,"Juan")
resultado=participacion(10,"Juan")
print(f"{resultado}")
print("\n")


#Aqui su arreglo 
def entrega(precio,apoderado):
  if precio >= 0 and precio <= 50:
    return f"Entrega en camino {apoderado} pagado con {precio}"
  else:
    return f"Su entrega va a demorar {apoderado}"
apoderado1=entrega(50,"Leo")
apoderado2=entrega(100,"Jazmin")

print(f"{apoderado1}")
print(f"{apoderado2}")
print(f"{apoderado1} | {apoderado2}")

#Que es esto?
apoderado6=""


