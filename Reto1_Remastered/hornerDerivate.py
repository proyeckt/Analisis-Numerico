#Función Derivada del metodo de Horner
from decimal import Decimal

def horner(coeficientes, grado, valor):
  iteraciones=1
  y = z = coeficientes[0]
  sumas=productos=0
  for j in range(1, grado):
    y = valor * y + coeficientes[j]
    z = valor * z + y
    productos+=2
    sumas+=2
    iteraciones+=1
  return Decimal.from_float(z),iteraciones,productos,sumas
coef= [3,7,2,-5]
grado=3
valor=31.9122
[deriv,itera,productos,sumas]=horner(coef,grado,valor)

print("Derivada de f(x) en x= ",valor," = ",deriv," realizada en ",itera," iteraciones")
print("Se realizaron ",productos," multiplicaciones y ",sumas," sumas")
derivCalc=9614.27
errorA=abs(9614.267379559998516924679279327392578125-derivCalc)
errorR=errorA/derivCalc
print("Error Absoluto:",errorA)
print("Error Relativo:",errorR)

