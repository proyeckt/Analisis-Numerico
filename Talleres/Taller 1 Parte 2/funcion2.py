#Funcion del metodo de Horner
def horner (coeficientes,grado,valor):
  resultado = coeficientes[0]
  i = 1
  while(i <= grado):
    resultado = (resultado * valor) + coeficientes[i]
    i += 1
  #end while
  return (resultado,i-1)
#end def
x=[]
cont=0
while(cont<=51):
  x.append(1)
  cont+=1
valor=1.0001
[res,iteraciones]=horner(x,51,valor)
print("Numero Iteraciones: ",iteraciones, "\t Resultado: ",res)
