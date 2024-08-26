import time
from datetime import datetime
def printcake():
    print("""                        0   0
                        |   |
                    ____|___|____
                 0  |~ ~ ~ ~ ~ ~|   0
                 |  |           |   |
              ___|__|___________|___|__
              |/\/\/\/\/\/\/\/\/\/\/\/|
          0   |       H a p p y       |   0
          |   |/\/\/\/\/\/\/\/\/\/\/\/|   |
         _|___|_______________________|___|__
        |/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|
        |                                   |
        |         B i r t h d a y! ! !      |
        | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ |
        |___________________________________|""")
answer = input("Hey! I heard that it's your birthday! Is it your birthday today? (Y/N) ")
time.sleep(1)
if answer.upper() == "Y":
    print("Happy Birthday!!!")
    time.sleep(2)
    print("Here's some cake just for you, to celebrate!")
    time.sleep(4)
    printcake()
    time.sleep(2)
    years = input("How old are you now? ")
    year_list = []
    for i in years:
        year_list.append(i)
    length = len(year_list)
    if year_list[length-1] == 1:
        suffix = "st"
    elif year_list[length-1] == 2:
        suffix = "nd"
    elif year_list[length-1] == 3:
        suffix = "rd"
    else:
        suffix = "th"
    time.sleep(1)
    print("Wow!")
    time.sleep(1)
    print(years,"years old!")
    time.sleep(1)
    print("That means you've been around since...")
    time.sleep(1)
    for i in range(0,3):
        time.sleep(1)
        print(".")
    current_year = int(time.strftime("%Y"))
    birth_year = current_year - int(years)
    time.sleep(1)
    print(str(birth_year)+"!")
    days_alive = int(years)*365
    time.sleep(1)
    print("That's", days_alive, "days!")
    time.sleep(1)
    print("What an absolute icon!")
    time.sleep(1)
    print("Hope to see you in",str(current_year+1),"for your",str(int(years)+1)+suffix,"birthday!")
    time.sleep(10)
if answer.upper() == "N":
    print("Well, this only really works on your birthday, so try again later. ;P")
    time.sleep(10)