from vpython import *
import time
length = 300
x = float(-0.05*length)
y = float(0)
z = float(0)
#position = vector(x,y,z)
#james = sphere(pos = position, color = color.red)

for i in range(-1,length):
    y = (x**2)*0.025
    position = vector(x,y,z)
    #time.sleep(0.1)
    sphere(pos = position, color = color.green)
    x += 0.1
    print(position)