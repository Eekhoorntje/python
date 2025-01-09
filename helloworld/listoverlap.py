a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

seta = set(a)
setb = set(b)

if len(seta) < len(setb):
    for x in seta:
        if x in setb:
            print("{} is in both lists".format(x))
else: 
    for x in setb:
        if x in seta:
            print("{} is in both lists".format(x))