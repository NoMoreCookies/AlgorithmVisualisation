import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def Wave(frame):
    x_data = np.arange(-5+frame/10,5+frame/10,0.1)
    X, Y = np.meshgrid(x_data,y_data)
    Z = np.sin(X) 
    ax.cla()
    ax.plot_surface(X,Y,Z,cmap = "plasma")

ax = plt.axes(projection = "3d")
x_data = np.arange(-5,5,0.1)
y_data = np.arange(-5,5,0.1)

X, Y = np.meshgrid(x_data,y_data)

Z = np.sin(X) 

print(X)

ax.plot_surface(X,Y,Z,cmap = "plasma")


animate = FuncAnimation(plt.gcf(),func = Wave ,interval = 1)
plt.show()