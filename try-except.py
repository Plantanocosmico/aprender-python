try:
  numero=int(input("Escribe un numero:"))
  print(f"Tu numero es {numero}")
except ValueError:
  print("Eso no es un numero") 

try:
    numero = int(input("Escribe un número: "))
    resultado = 100 / numero #Float
    print(f"100 entre {numero} es {resultado}")
except ValueError:
    print("Eso no es un número")
except ZeroDivisionError:
    print("No puedes dividir entre cero")
finally:
    print("Esto siempre se ejecuta, haya error o no")



