# PyPlotter 
# A simple script to plot serial data in real time.
# (c) Chris Monaco 2018

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import csv

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x = []
y = []
count = 0

# Initialize serial communication
ser = serial.Serial('/dev/ttyACM0', 9600)

# Function to read and store data
def animate(i, x, y):

    global count
    count += 0.25
    #get serial reading
    temp = ser.readline()
    print(temp)
    try:
        y.append(float(temp))
    except:
        y.append(0)

    #store time of sample
    x.append(dt.datetime.now().strftime('%S'))

    #draw x and y lists
    ax.clear()
    ax.plot(x,y)

    #format plot
    plt.xticks(rotation = 45, ha = 'right')
    plt.subplots_adjust(bottom=0.3)
    plt.title('Temperature vs. Time')
    plt.ylabel('Temperature (C)')

    #store data in text file
    with open('log.csv', 'a') as fd:
       fd.write(str(count)+ ',' + str(float(temp)) + '\n')

#set up animation function call
ani = animation.FuncAnimation(fig,animate, fargs=(x,y), interval = 250)
plt.show()
