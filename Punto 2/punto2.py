# Interpolacion y Polinomio de Lagrange
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Funcion Polinomio Lagrange
def polinomio_lagrange(xi,yi):
  n = len(xi)
  polinomio = 0
  for i in range(0,n,1):
      # Termino de Lagrange
      termino = 1
      for j  in range(0,n,1):
          if (j!=i):
              termino = termino*(x-xi[j])/(xi[i]-xi[j])
      polinomio = polinomio + termino*yi[i]
  return polinomio

#La tangente es aproximadamente 1 en 0.78 
xi = np.array([0.78, 0, 1,2])
yi = np.array([7,10, 15,5])

x = sym.Symbol('x')

polinomio=polinomio_lagrange(xi,yi)
#print(polinomio)
px = polinomio.expand()
print('Polinomio de Lagrange:\n',px)
# Gráfica
pxn = sym.lambdify(x,polinomio)
xi_p = np.linspace(np.min(xi),np.max(xi),100)
yi_p = pxn(xi_p)

plt.title('Interpolación Lagrange')
plt.plot(xi,yi,'o', label = 'Puntos')
plt.plot(xi_p,yi_p, label = 'Polinomio')
plt.legend()
plt.show()
plt.savefig('plot.png')