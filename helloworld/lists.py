a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
targetlist = []
testnum = int(input("provide max val: "))
for val in a: 
    if val < testnum:
        targetlist.append(val)
        #print("{} is less than {}".format(val, testnum))
print(targetlist)
              