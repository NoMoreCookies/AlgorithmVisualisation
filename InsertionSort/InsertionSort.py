import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np
from itertools import count

# Here we generate list of random integers

def InsertionSort(frame):
        print(frame)
        j = frame
        while j > 0 and y[j - 1] > y[j]:
            y[j], y[j - 1] = y[j - 1], y[j]
            j -= 1
        print(y)
        graph.cla()
        graph.bar(x,y)
        if(frame == n-1):
              animate.pause()

tab = [0,5]
x = np.linspace(1,20,20)
y = random.sample(range(1,100),20)
n = len(x)
graph = plt.subplot()
graph.bar(x,y)

graph.set(xlim=(0, 21), xticks=np.arange(1, 21,1), ylim=(0, 101) ,  yticks=np.arange(10, 110 ,10))

animate = FuncAnimation(plt.gcf(),func = InsertionSort,frames =n  ,interval = 100)
plt.show()





