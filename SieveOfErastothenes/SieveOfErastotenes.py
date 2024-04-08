import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def SieveOfErastotenes(number):

    NMB = number 
    print(NMB)
    if(NMB == 1 or NMB == 0):
        pass
    else:
        NMB = 2 * NMB
        while(NMB <= n):
            if(y[NMB]==0):
                NMB =  NMB + number
                next
            else:
                y[NMB]=0
                NMB =  NMB + number
    
    graph.cla()
    graph.set_xticks(y)
    graph.bar(x,y)
    if(number == int(n/2)):
              animate.pause()


n = int(input("Podaj ilość liczb "))

x = np.linspace(0,n,n+1)
y = list(range(0,n+1))
graph = plt.subplot()
y[0] = 0
y[1] = 0
graph.bar(x,y)


graph.set(xlim=(1, n+1), xticks=np.arange(10, n+1,10), ylim=(0, n+1) ,  yticks=np.arange(10, n+1 ,10))
print(int(n/2)+1)
animate = FuncAnimation( plt.gcf() , func = SieveOfErastotenes , frames = int(n/2)+1  , interval = 10 )
plt.show()





