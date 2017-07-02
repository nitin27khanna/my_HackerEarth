##Convert number n to different bases and then add it digit wise to get the average

def hcf(a,b):
    
    less_one = a if a < b else b
    gcd = 1
    for i in range (1,less_one+1):
        if a % i == 0 and b % i ==0:
            gcd = i
        
    return gcd
    
def getbase(number,n):
    
    rem = 0
    copy = number
    
    while copy > 0:
        rem = rem + (copy%n)
        copy = copy // n
    
    return rem    

def arr_avg_den(arr):
    sum1 = 0
    for each in arr:
        sum1 +=  each
    
    #print (arr,sum1)
    if sum1 % len(arr) == 0:
        return 1
    else:
        return (len(arr)//hcf(sum1,len(arr)))

#number of testcases
tests=int(input())

for i in range (0,tests):
    ##taking input
    number = int(input())
    
    #list to hold answers
    arr = []
    
    for n in range (2,number):
        arr.append(getbase(number,n))
        
    print (arr_avg_den(arr))
