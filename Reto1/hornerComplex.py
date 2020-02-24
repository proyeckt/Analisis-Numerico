#Funcion Horner Complex
def hornerComplex(coeficientes, grado, valor):
  y = z = coeficientes[0]
  for j in range(1, grado):
    y = valor * y + coeficientes[j]
  z = valor * z + y
  return (y,z)
coefComplex= [(2+3j),0+1j,5,2]
grado=3
valor=2
valorComplex=1+1j
[normal,deriv]=hornerComplex(coefComplex,grado,valorComplex)
print("Evaluación de f(x) en x = ",valorComplex," = ",normal)
print("Derivada de f(x) en x = ",valorComplex," = ",deriv)
