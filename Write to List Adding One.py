import os
scriptDirectory = os.path.dirname(os.path.realpath(__file__))
with open(scriptDirectory+"/Test.txt","w+") as tester:
    n = 0
    while True:
        tester.write(str(f"{n:,}"))
        tester.write("\n")
        n += 1
        #print(n)