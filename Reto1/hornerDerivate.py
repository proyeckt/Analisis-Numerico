#Función Derivada del metodo de Horner
def horner(coeficientes, grado, valor):
  iteraciones=1
  y = z = coeficientes[0]
  for j in range(1, grado):
    y = valor * y + coeficientes[j]
    z = valor * z + y
    iteraciones+=1
  return z,iteraciones
coef= [3,7,2,-5]
grado=3
valor=2
[deriv,itera]=horner(coef,grado,valor)
print("Derivada de f(x) en x= ",valor," = ",deriv," realizada en ",itera," iteraciones")
