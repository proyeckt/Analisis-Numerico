#Juan Pimienta
#Edwin Turizo

#import sympy as sp
import numpy as np
from matplotlib import pyplot as plt

def factorial(num):
  if(num==0):
    return 1
  else:
   return num* factorial(num-1)

def combinatoria (n,i):
  if(i>=0 and i<=n):
    return (factorial(n)/(factorial(i)*factorial(n-1)))
  else:
    return 0

def bernstein(n,i,t):
  return combinatoria(n,i)* t**i * (1-t)**(n-i)

def superfBezier(m,n):
  puntosX=[]
  puntosY=[]
  puntosZ=[]

  arreglo=np.arange(0,1,0.005)
  arregloV=np.arange(0,1,0.005)
  for u in arreglo:
    for v in arregloV:
      x=y=z=0
      for i in range(len(n)):
        for j in range(len(m)):
          x=x+bernstein(len(n),i,u)*bernstein(len(m),j,v)*m[j][0]*n[i][0]
          y=y+bernstein(len(n),i,u)*bernstein(len(m),j,v)*m[j][1]*n[i][1]
          z=z+bernstein(len(n),i,u)*bernstein(len(m),j,v)*m[j][2]*n[i][2]
      puntosX.append(x)
      puntosY.append(y)
      puntosZ.append(z)
  return puntosX,puntosY,puntosZ


m = np.array([[0, 8, 2], [1.7, 7.5, 2], [2, 4.5, 2], [4, 4, 2]])
n=np.array([[4.8, 1.8,2], [8, 0.6, 2], [8, 0, 2]])

puntosX,puntosY,puntosZ=superfBezier(m,n)


fig=plt.figure() 
ax = fig.gca(projection='3d')
ax.plot(puntosX, puntosY, puntosZ, label='bezier')
plt.savefig('plot.png')
plt.show()

# for rotate the axes and update.
#ax.view_init(30,90*4)
#plt.show()
#plt.savefig('plot2.png')
