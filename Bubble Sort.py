import random
def bubble(data_set):
    data = list(data_set)
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data
def reverse_bubble(data_set):
    data = list(data_set)
    for i in range(len(data)):
        for j in range(i+1,len(data)):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
    return data
sort = []
for i in range(10):
    sort.append(random.randint(0,100))
print("Random List:",sort)
print("Bubble Sorted List:",bubble(sort))
print("Reverse Bubble Sorted List:",reverse_bubble(sort))