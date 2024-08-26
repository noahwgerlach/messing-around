letters = ["a","b","c","d"]
numbers = [1,2,3,4]
symbols = ["!","@","#","$"]
grand = [letters, numbers, symbols]

for i in range(len(grand)):
    for j in range(len(grand[i])):
        print(grand[i][j])

for i in range(len(grand)+1):
    for j in range(len(grand[i-1])):
        if j > len(grand)-1:    
            pass
        else:
            print(grand[j][i])