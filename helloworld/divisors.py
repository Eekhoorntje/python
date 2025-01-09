testnum = int(input("provide max val: "))
for x in range(2, int(testnum/2)+1): 
    if(testnum % x == 0):
        print("{} is a factor of {}".format(x,testnum))