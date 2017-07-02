number = input()
numArray = (input().split(' '))
numPro = 1

for i in numArray:
    numPro =  (numPro *int(i)) % ((10**9)+7)

print (numPro)

#find product of array elements
