#Metodo Horner Numeros Complejos
def contadorOperaciones(sumas,productos,valor,num):
  if type(valor)==complex and type(num)==complex:
    sumas+=3
    productos+=4
  elif (type(num)==complex and type(valor)!=complex) or (type(num)!=complex and type(valor)==complex):
    sumas+=1
    productos+=2
  elif type(num)!=complex and type(valor)!=complex:
    productos+=1
  return sumas,productos

def hornerComplex(coeficientes, grado, valor):
  iteraciones=1
  y = z = coeficientes[0]
  sumas=productos=0
  for j in range(1, grado):
    [sumas,productos]=contadorOperaciones(sumas,productos,valor,y)
    [sumas,productos]=contadorOperaciones(sumas,productos,valor,z)
    y = valor * y + coeficientes[j]
    z = valor * z + y
    sumas+=4
  [sumas,productos]=contadorOperaciones(sumas,productos,valor,y)
  y = coeficientes[-1] + (valor* y)
  sumas+=2
  iteraciones+=1
  return (y,z,productos,sumas,iteraciones)
coefComplex= [(2+3j),(0+1j),5,2]
coefff=[(6+9j),(0+2j),5]
grado=3
valorComplex=1+1j
[normal,deriv,productos,sumas,iteraciones]=hornerComplex(coefComplex,grado,valorComplex)
print("Evaluación de f(x) en x = ",valorComplex," = ",normal)
print("Derivada de f(x) en x = ",valorComplex," = ",deriv)
print("Se realizaron ",iteraciones," iteraciones en el ciclo.")
print("Se realizaron ",productos," multiplicaciones y ",sumas," sumas")
