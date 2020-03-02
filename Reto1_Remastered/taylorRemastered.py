import math
import numpy as np
import matplotlib.pyplot as plt
import os
from decimal import Decimal

def func_sin(x, n):
    sin_aprox = 0
    coefs=[]
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i+1)
        denom = math.factorial(2*i+1)
        sin_aprox += (Decimal.from_float(coef)) * ( Decimal.from_float((num))/Decimal.from_float((denom)))
        coefs.append(sin_aprox)
    return (sin_aprox,coefs)

errorEsperado=1e-12
li=-((math.pi)/64)
ls=((math.pi)/64)

angles = np.arange(li,ls,0.01)
p_sin = np.sin(angles) 
fig, ax = plt.subplots()
ax.plot(angles,p_sin)

iteracion=1
print()
print("Iteracion ","\t\t\t\t\tAproxTaylor","\t\t\t\t\tCalcValue","\t\t\t\t\t\t\t\t\t\t\tError")
while True:
    t_sin=[]
    sin_exp=[]
    errores=[]
    for angle in angles:
      sinAprox,coefs=func_sin(angle,iteracion)
      t_sin.append(sinAprox)
      sinExp=Decimal.from_float(math.sin(angle))
      sin_exp.append(sinExp)
    
    error=abs(t_sin[-1] - sin_exp[-1])
    print(iteracion,"\t\t",t_sin[-1],"\t\t",sin_exp[-1],"\t\t",error)
    ax.plot(angles,t_sin)
    if error < errorEsperado:
        break
    iteracion+=1

print("Grado del polinomio de la mejor aproximacion",iteracion-1)
print("Coeficientes del polinomio de la mejor aproximacion de Taylor",coefs)
#ax.set_ylim([-7,4])
#ax.set_xlim([-np.pi/64,np.pi/64])

legend_lst = ['sin() function']
for i in range(1,iteracion+1):
    legend_lst.append(f'Taylor Series - {i} terms')
ax.legend(legend_lst, loc=3)
#plt.savefig(os.path.join(os.path.dirname(os.path.realpath(__file__)),'taylor_sin_approximation.png'))
