import copy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import numpy as np
import math

def Single_Merge(sub1 ,  indL,  indR, indE,  sub2):
    i = indL 
    j = indR 
    currInd = indL
    while(  currInd < indE ):
    
        if( i < indR and ( indE <= j or (sub1[i] <=  sub1[j]))):
        
            sub2[currInd] = sub1[i]
            i+=1
        
        else:
        
            sub2[currInd] = sub1[j] 
            j+=1
        currInd+=1

def Bottom_Up_Merge_Sort(frame):
    width =  (2 ** (frame))
    sub2=copy.deepcopy(y)
    l=len(y)
    i=0
    while (i < l):
        Single_Merge( y , i ,  i+width  ,  min( i + 2*width , l ) , sub2) 
        i  = i + 2 * width
    i=0
    while ( i < l ):
        y[i]=sub2[i]
        i+=1
    graph.cla()
    graph.bar(x,y)
    if(frame == helP -1 ):
        animate.pause()

x = np.linspace(1,20,20)
y = random.sample(range(1,100),20)

graph = plt.subplot()
graph.bar(x,y)
helP = int(math.log(len(y),2))+1
graph.set(xlim=(0, 21), xticks=np.arange(1, 21,1), ylim=(0, 101) ,  yticks=np.arange(10, 110 ,10))
animate = FuncAnimation(plt.gcf(),func = Bottom_Up_Merge_Sort,frames = helP  ,interval = 10)
plt.show()





