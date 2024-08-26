import time

#seed = 0
seed = 2**75
steps = 0
print("test")
while(True):
    steps = 0
    x = seed
    step_nums = [x]
    while x != 1:
        if x % 2 == 1:
            x = x*3 + 1
            step_nums.append(x)
            steps += 1
        if x % 2 == 0:
            x = int(x*0.5)
            step_nums.append(x)
            steps += 1

    print(step_nums)
    print()
    print("Seed: " + str(seed))
    print("Steps: " + str(steps))
    print()
    time.sleep(0.1)
    seed += 1