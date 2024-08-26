import random
import time
print("This program will randomly generate numbers until it matches your number.")
time.sleep(1)
guess = int(input("What number (between 1 and 100,000) would you like to try? "))
place = 0
while True:
    x = random.randint(0,10**5)
    print(x)
    print("Number #"+str(place+1))
    if x == guess:
        break
    place += 1
print("Randomly Generated Number #"+str(place+1),"was",str(guess)+".")
filler = 0
filler_list =[]
while True:
    filler_list.append(filler)
    time.sleep(5)
    filler += 1
