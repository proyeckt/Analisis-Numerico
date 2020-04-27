from Bezier import Bezier
import numpy as np
import matplotlib.pyplot as plt


points_set_1=np.array([[485,960],[536,1002],[489,1012],[257,830],[289,762],[431,773]])
points_set_2=np.array([[431,773],[330,750],[29,512],[46,483],[431,561]])

t_points = np.arange(0, 1, 0.01)

curve_set_1 = Bezier.Curve(t_points, points_set_1)
curve_set_2 = Bezier.Curve(t_points, points_set_2)

#Graficar
fig = plt.figure(dpi=128)

plt.gca().set_aspect('equal', adjustable='box')

plt.plot(curve_set_1[:, 0], curve_set_1[:, 1],color='b')
plt.plot(curve_set_2[:, 0], curve_set_2[:, 1],color='b')

plt.savefig('plotBezier.png')
