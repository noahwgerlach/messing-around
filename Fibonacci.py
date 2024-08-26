delay_time = float(input("What delay would you like between each number? (Seconds) "))
import time
fibonacci_list = [0,1]
list_position = 2
while True:
    addition_to_list = fibonacci_list[list_position-2] + fibonacci_list[list_position-1]
    fibonacci_list.append(addition_to_list)
    print(f"{fibonacci_list[list_position-2]:,}")
    list_position += 1
    time.sleep(delay_time)