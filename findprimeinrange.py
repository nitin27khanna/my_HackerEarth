
def findPrime(number):
    primes = []
    for i in range (2,number):
        flag = 0
        if i//2 >= 2:
            for j in range(2,(i//2)+1):
                if (i%j) == 0:    
                    flag = 1
                    
            
            if(flag == 0):
                primes.append(i)
        else:
            primes.append(i)
            
    for i in (primes):
        print(i,end=" ")
    print("")
    
num = int(input())
prime_list = []
prime_list = findPrime(num)
#print("I am here")
#print (prime_list)
                
            
