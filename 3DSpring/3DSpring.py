import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def Spring(frame):
    theta =np.linspace(0+frame,2*np.pi*6+frame,150)

    X = np.linspace(1,10,150)
    Y = radius * np.cos(theta)
    Z = radius * np.sin(theta)
    ax.cla()
    ax.plot(X,Y,Z,color = "purple")
    ax.plot(X,Y1,color = "green")


theta =np.linspace(0,2*np.pi*6,150)
radius = 0.4
X = np.linspace(1,10,150)
Y = radius * np.cos(theta)
Z = radius * np.sin(theta)


ax = plt.axes(projection = "3d")

ax.set_xlabel("X",color='red')
ax.set_ylabel("Y",color='red')
ax.set_zlabel("Z",color='red')

ax.plot(X,Y,Z,color = "purple")

Y1 = np.linspace(0,0,150)
ax.plot(X,Y1,color = "green")


animate = FuncAnimation(plt.gcf(),func = Spring ,interval = 10)
plt.show()