testnum = int(input("input test val:"))

while testnum != -1: 
    if ( testnum % 2 == 0):
        print("{} is even".format(testnum))
    else: 
        print("{} is odd".format(testnum))

    testnum = int(input("input test val (-1 to quit):"))