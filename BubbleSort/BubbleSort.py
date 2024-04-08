import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np
from itertools import count

# Here we generate list of random integers


def BubbleSort(frame):
    length = len(y)
    if(frame<length):
        i = 1
        val = y[0]
        k=0
        while(i<length-frame):
                if(y[i]>val):
                    val=y[i]
                    k=i
                i+=1   
        i-=1
        y[k]=y[i]
        y[i]=val
        i=1
        print(y)
        graph.cla()
        graph.bar(x,y)
        if(frame == n-1):
             animate.pause()


tab = [0,5]
x = np.linspace(1,20,20)
y = random.sample(range(1,100),20)
n = len(x)**2
graph = plt.subplot()
graph.bar(x,y)

graph.set(xlim=(0, 21), xticks=np.arange(1, 21,1), ylim=(0, 101) ,  yticks=np.arange(10, 110 ,10))

animate = FuncAnimation(plt.gcf(),func = BubbleSort,frames =n  ,interval = 100)
plt.show()





