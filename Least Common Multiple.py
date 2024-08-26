while True:
    first = float(input("What is the first number? "))
    second = float(input("What is the second number? "))
    x = first
    y = second
    while True:
        if x == y:
            break
        if x > y:
            y = y + second
            print("Second:",y)
        if y > x:
            x = x + first
            print("First:",x)
    print("The least common multiple between",first,"and",second,"is",x)
