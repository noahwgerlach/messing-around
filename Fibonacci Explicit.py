import time
import math
item = 0
sfive = math.sqrt(5)
while True:
    numerator = (((1+sfive)/2)**item) - (((1-sfive)/2)**item)
    fibo = int(numerator/sfive)
    print(fibo)
    time.sleep(0.5)
    item += 1