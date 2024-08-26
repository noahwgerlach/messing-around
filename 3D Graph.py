from vpython import *
import time
import math
x = int(-5)
y = int(0)
z = int(0)
#position = vector(x,y,z)
coord = [x,y,z]
for i in range(-1,10):
    print(vector(coord[0],coord[1],coord[2]))
    print(coord)
    coord[0] += 1
    coord[1] = coord[0]**2
    sphere(pos = vector(coord[0],coord[1],coord[2]))