#Un rango simple de datgos que hace un rango con la variable i a un range o veces de 5 veces empezando desde el cero 

for i in range(5):
    print(i)

print("")
#Ahora mientras o while configura una palabra con un contandor determinado o una condicon  

contador = 0
while contador < 5: #condicona cuando el contador sea menor de 5 imprimira la varibale int del contador y luego hara suma de 1 
    print(contador)
    contador += 1

#Ahora por ejemplo como se utilizaria esta función con lo que aprendimos ayer

personas={"Nombre":"Pablo","edad":22,"peso":55}
while personas["peso"] < 61:
    #Aumentara hasta qeu sea sea 60 
    for años in range(personas["peso"]>24):
        print(f"La edad de {personas['Nombre']} es {personas['edad']} y su peso actual es {personas["peso"]}")
        personas["peso"] += 1 # o tambien personas["peso"] = personas["peso"]+1 
        personas["edad"] += 1

#con una lista

humanos=["Oscar","Ruben","Leandro"]
for gente in humanos:
    print(f"Aqui una lista de nombres {gente}")
    
