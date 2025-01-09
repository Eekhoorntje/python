testStr = input("Enter a string to check for palindromicity: ")
strLen = len(testStr)
idx = 0
palindrome = True

while idx < int(strLen/2):
    if(testStr[idx] != testStr[strLen-1-idx]):
        palindrome = False
        print("{} is not a palindrome".format(testStr))
        break
    idx = idx+1

if palindrome:
    print("{} is a palindrome".format(testStr))

