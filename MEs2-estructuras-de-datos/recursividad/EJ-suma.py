#Ejemplo de funcionamiento
def contador(n):
  if n ==0:
    print("Despegue")
    return
  print(n)
  contador(n-1)
contador(3)
#La suma en total 
def suma_hasta(n):
  if n == 0:
    return 0
  print(n)
  if n >= 0:
    resultado=n + suma_hasta(n-1)
    print(f"n={n} devuelve {resultado}")
    return resultado

  if n < 0: 
    resul=n+suma_hasta(n+1)
    print(f"numero{n} devuelve {resul}")
    return resul
  
assert suma_hasta(5) == 15

assert suma_hasta(0) == 0 

assert suma_hasta(-6) == -21

 