import numpy as np
from matplotlib import pyplot as plt

from scipy.interpolate import lagrange
from scipy.interpolate import InterpolatedUnivariateSpline


points=np.array([[23,216],[103,318],[132,504],[142,623],[174,742],[189,818],[178,887],[153,962],[145,1078],[141,1231],[191,1291],[230,1286],[255,1232],[261,1121],[285,1006],[315,859],[363,1006],[357,1154],[385,1422],[429,1460],[504,1413],[487,1252],[504,1155],[496,903],[728,1445],[776,1453],[820,1386],[775,1243],[648,900],[654,843],[991,1282],[1033,1283],[1056,1229],[957,991],[835,834],[781,654],[766,555],[810,488],[1068,630],[1101,658],[1212,634],[1221,592],[1024,424],[924,361],[858,272],[583,100],[510,96],[462,103],[268,0]])
    
n=len(points)
x_coords = [p[0] for p in points] #x_coords=points[:,0]
y_coords = [p[1] for p in points]

plt.plot(x_coords, y_coords, '-')
plt.savefig('plot2.png')

plt.cla() #Borra la grafica anterior

plt.plot(x_coords, y_coords, '-o')
plt.savefig('plot.png')


timestamp = np.arange(0,n,1)

start_timestamp = min(timestamp)
end_timestamp = max(timestamp)
duration_seconds = (end_timestamp - start_timestamp)

new_intervals = np.linspace(start_timestamp, end_timestamp, duration_seconds)
new_x_coords = np.interp(new_intervals, timestamp, x_coords)
new_y_coords = np.interp(new_intervals, timestamp, y_coords)

plt.cla() #Borra la grafica anterior
plt.plot(new_x_coords, new_y_coords, '-o')
plt.savefig('plot_new.png')
plt.cla() #Borra la grafica anterior
plt.plot(new_x_coords, new_y_coords, '-')
plt.savefig('plot_new2.png')
