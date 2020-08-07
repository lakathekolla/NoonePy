'''
Title : Bluetooth Helping Text to plot
Author : R M Lakruwan @ Noone
Date : 07 Aug 2020
Compatibality : Python 3
version : 1.0
'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    # get data from text file to python array
    pullData = open("a.txt","r").read()
    dataArray = pullData.split('\n')
    
    # for cordinate
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)

# Time plot refreshing data under interval
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
