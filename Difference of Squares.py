import time
x = 0
while True:
    square1 = x**2
    square2 = (x+1)**2
    diff = square2 - square1
    print(square2,"("+str(x+1)+")","-",square1,"("+str(x)+")","=",diff)
    x += 1
    time.sleep(1)