# PyPlotter 2
# Just like PyPlotter but with a 'simple' moving average calculation
# (c) Chris Monaco 2018

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial
import csv

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x = []
y = []

time = 0 # Holds our time (aka number of secs)
data = []
window = 4

# Initialize serial communication
ser = serial.Serial('/dev/ttyACM0', 9600)

# Function to read and store data
def animate(i, x, y):

    global time
    time += 0.25

     #get serial reading
    temp = ser.readline()
    print(temp)
    try:
        data.append(float(temp))
    except:
        data.append(0)

    if(time % 1 == 0 and len(data) >= window):

        y.append(sum(data[-window:]) /  window)

        #store time of sample
        x.append(time)

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
            fd.write(str(x[-1])+ ',' + str(y[-1]) + '\n')

#set up animation function call
ani = animation.FuncAnimation(fig,animate, fargs=(x,y), interval = 250)
plt.show()
