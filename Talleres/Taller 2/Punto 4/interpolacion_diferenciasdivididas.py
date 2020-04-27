import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import math

#Funcion
f= lambda x: math.log(x)

#Generacion Puntos
xi=np.array(np.linspace(1,2,10))
fi=np.array([f(i) for i in xi])

titulo = ['i','xi','fi']
n = len(xi)
# cambia a forma de columnas
i = np.arange(1,n+1,1)
i = np.transpose([i])
xi = np.transpose([xi])
fi = np.transpose([fi])
# Añade matriz de diferencias
dfinita = np.zeros(shape=(n,n),dtype=float)
tabla = np.concatenate((i,xi,fi,dfinita), axis=1)
# Sobre matriz de diferencias, por columnas
[n,m] = np.shape(tabla)
c = 3
diagonal = n-1
while (c<m):
    titulo.append('df'+str(c-2))
    # calcula cada diferencia por fila
    f = 0
    while (f < diagonal):
        tabla[f,c] = tabla[f+1,c-1]-tabla[f,c-1]
        f = f+1
    
    diagonal = diagonal - 1
    c = c+1

dfinita = tabla[:,3:]
n = len(dfinita)
x = sym.Symbol('x')
h = xi[1,0]-xi[0,0]
polinomio = fi[0,0]
for c in range(1,n,1):
    denominador = np.math.factorial(c)*(h**c)
    factor = dfinita[0,c-1]/denominador
    termino=1
    for f  in range(0,c,1):
        termino = termino*(x-xi[f])
    polinomio = polinomio + termino*factor

polinomio = polinomio.expand()
px = sym.lambdify(x,polinomio)

print([titulo])
print(tabla)
print('Polinomio:\nP(x)=',polinomio)

# Gráfica
xi_p = np.linspace(np.min(xi),np.max(xi),100)
fi_p = px(xi_p)
plt.title('Interpolación Diferencias Divididas')
plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(xi_p,fi_p, label = 'Polinomio')
plt.legend()
plt.show()
plt.savefig('plot.png')

#Evaluaciones y Error
original1=math.log(1.0)
original2=math.log(2.0)
aprox1=px(1)
aprox2=px(2)

#Error Absoluto
error1Absoluto=abs(original1-aprox1)
error2Absoluto=abs(original2-aprox2)
if original1==0:
  original1+=1e-10
if original2==0:
  original2+=1e-10
#Error Relativo
error1Relativo=error1Absoluto/abs(original1)
error2Relativo=error2Absoluto/abs(original2)
print("Valor x=1")
print("Error Absoluto",error1Absoluto)
print("Error Relativo",error1Relativo)
print("Valor x=2")
print("Error Absoluto",error2Absoluto)
print("Error Relativo",error2Relativo)
