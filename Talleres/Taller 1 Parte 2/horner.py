#Metodo 3 - Algoritmo de Horner 

import random
#Función del metodo de Horner
def horner(coeficientes, grado, valor):
  resultado = coeficientes[0]
  i = 1
  while(i <= grado):
    resultado = (resultado * valor) + coeficientes[i]
    i += 1
  #end while
  return (resultado,i-1)
#end def

coef=[2,-3,3,-4,-2,1,4]
grado=6
valor=1
minCoef=0
maxCoef=8;
for i in range(0,40):
  [res,iteraciones]=horner(coef,grado,valor)
  print("Numero Iteraciones: ",iteraciones, "\t Grado: ",grado)
  grado+=1;
  coef.append(random.randint(minCoef,maxCoef))
#end for

