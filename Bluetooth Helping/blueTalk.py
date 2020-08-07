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
    filan=[1]
    
    axisNowLab=len(AxisGreen)
    axisNowLabAr= AxisGreen
    axisNowLabArHolder =[]
    
    bluetooth=init_B("COM44");
    clear_B(bluetooth);

    while count<5:
        
        InputCorrected =-1
        input_data=bluetooth.readline()               #read incoming data
        
        #read incoming data with strip extra
        ##input_data=bluetooth.readline().rstrip()       
        
        if input_data.splitlines()==['G']:
            axisNowLab+=1
            print 'G'
            break
        
        if input_data.splitlines()==['N']:
            filan[0]=30
            print 'Near'
            break
        if input_data.splitlines()==['O']:
            filan[0]=100
            print 'OuT'
            break
        input_datam= re.findall('\d+', filan)
        input_datam.extend(['0'])                     #Sync Error Handle And Fomatttin
        for val in range(len(input_datam)):
            valNow= int(input_datam[val])
            if valNow>InputCorrected:
                InputCorrected=valNow
            if InputCorrected>300:
                InputCorrected=300
        countArray+=InputCorrected
        count+=1

    input_dd  =filan[0]#countArray/5                          #bytes coming decode average
    print input_dd
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
        print AxisGreen
        
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



