import serial
import time
import re
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init_B(comPort):
    bluetooth=serial.Serial(comPort, 9600)           #Start communications with the bluetooth unit
    return bluetooth

def cls_B(bluetooth):
    bluetooth.close()                                #End communications with the bluetooth unit

def clear_B(bluetooth):
    bluetooth.flushInput()                           #Clear Buffer with the bluetooth unit      

def animate(i):
    global xar
    global yar
    global AxisGreen
    global ax1
    input_dd_TmpArr=[]
    IncreTime_TmpArr=[]
    count=0
    countArray=0
    filan=[0,0,0,0,0]
    inputCount=5
    
    axisNowLab=len(AxisGreen)
    axisNowLabAr= AxisGreen
    axisNowLabArHolder =[]
    
    bluetooth=init_B("COM44");
    clear_B(bluetooth);
    
    while count<inputCount:
        input_data=bluetooth.readline().rstrip()    #read incoming data
        if 'x' in input_data:
            input_data='0'
        if input_data=='G':
            axisNowLab+=1
            break
        elif input_data=='B':                       #Bluetooth Mode On
            break
        else:
            try:
                filan[count]=int(input_data)        #Sync Error Handle And Fomatttin
            except ValueError:
                filan[count]=0
            count+=1

    outcount=0
    outavgNum=0
    FinalAvg=0
    for val in range(len(filan)):
        if filan[val]>0 and filan[val]<300:
            outavgNum+= filan[val]
            outcount+=1
        elif filan[val]>300:
            outavgNum+=300
            outcount+=1
            
    if outcount==0:
        FinalAvg=0
    else:
        FinalAvg=outavgNum/outcount
        
    input_dd  =FinalAvg                             #bytes coming decode average
    input_dd_TmpArr.append(int(input_dd))
    yar.extend(input_dd_TmpArr)

    global IncreTime
    IncreTime_TmpArr.append(IncreTime)
    axisNowLabArHolder.append(IncreTime)
    xar.extend(IncreTime_TmpArr)

    IncreTime+=1                                     #Save Increments on Global
     
    time.sleep(0.1)                                  #Delay to Read
    cls_B(bluetooth)                                 #Close Connection

    ax1.clear()
    
    if axisNowLab>len(AxisGreen):
        AxisGreen.extend(axisNowLabArHolder)
        print "Green Found at :", AxisGreen
        
    ax1.plot(xar,yar)                                #Green Line Pass
    for eachGreen in AxisGreen:
        plt.axvline(x=eachGreen, c='g')


IncreTime=0                                          #Define Global Variables to Catch TimeChange
xar=[]                                               #Define Global Variables to Catch Time in X
yar=[]                                               #Define Global Variables to Catch Path in Y
AxisGreen=[]                                         #Define Global Variables to Catch Path in X Green

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()



