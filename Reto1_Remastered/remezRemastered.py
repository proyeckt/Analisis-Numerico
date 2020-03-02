#Metodo de Remez
import math
import numpy as np
from matplotlib import pyplot as plt
import os

#Nodos de chebyshev
def _get_chebyshev_nodes(n, a, b):
  nodes = [.5 * (a + b) + .5 * (b - a) * math.cos((2 * k + 1) / (2. * n) * math.pi) for k in range(n)]
return nodes

def _get_errors(exactvals, polycoeff, nodes):
  ys = np.polyval(polycoeff, nodes)
for i in range(len(ys)):
  ys[i] = abs(ys[i] - exactvals[i])
return ys

def run_remez(fun, a, b, d, error):
  finished = False
cn = _get_chebyshev_nodes(d + 2, a, b)
cn2 = _get_chebyshev_nodes(100 * d, a, b)

iteracion = 0
while not finished and len(cn) == d + 2 and iteracion < 50:
  iteracion += 1
b = np.array([fun(c) for c in cn])
A = np.matrix(np.zeros([d + 2,d + 2]))
for i in range(d + 2):
  x = 1.
x *= cn[i]
for j in range(d + 2):
  A[i, j] = x
x *= cn[i]
A[i, -1] = (-1)**(i + 1)
res = np.linalg.solve(A, b)

revlist = reversed(res[0:-1])
sccoeff = []
for c in revlist:
  sccoeff.append(c)
errs = _get_errors([fun(c) for c in cn2], sccoeff, cn2)
maximum_indices = []

if errs[0] > errs[1]:
  maximum_indices.append(0)
for i in range(1, len(errs) - 1):
  if errs[i] > errs[i-1] and errs[i] > errs[i+1]:
  maximum_indices.append(i)
if errs[-1] > errs[-2]:
  maximum_indices.append(-1)

finished = True
for idx in maximum_indices[1:]:
  if abs(errs[idx] - errs[maximum_indices[0]]) > error:
  finished = False
cn = [cn2[i] for i in maximum_indices]

return (list(reversed(res[0:-1])))

def f(x):
  return math.sin(x)
error=1e-12

a = -math.pi/64
b = math.pi/64
degree = 3
angles = np.arange(a,b,0.01)
coeffs = run_remez(f, a, b,degree,error)
print("Coefficients{}: {}", list(reversed(coeffs)))
