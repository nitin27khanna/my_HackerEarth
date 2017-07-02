
number = int(input())

for i in range (0,number):
    
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha = ALPHA.lower()
    ALPHA = ALPHA + alpha
#alpha = ALPHA.lower()
    primes = []
#print(alpha)
    magic_word = ""
    for n in  range(65,91):
        flp = True
        for i in range (2,n//2):
            if n % i == 0:
                flp = False
                break
        if flp == True:
            primes.append(n)

    for n in  range(97,123):
        flp = True
        for i in range (2,n//2):
            if n % i == 0:
                flp = False
                break
        if flp == True:
            primes.append(n)

   # print(primes)
    length =    input()     
    string = input()
    flag = True

#if chr(string[0]).issupper():
#    flag = False
#    string = string.upper()        
    
    for s in (string):
        if(s.isdigit()):
            ascci = 53
        elif(s.isupper()):
            ascci = ALPHA.index(s) + 65 
        else:
            ascci = ALPHA.index(s) + 65 + 6
        minimum = -1 
        loc = -1
        for i in primes:
            if ascci >= i:
                diff = (ascci - i) 
            else:
                diff = (ascci - i) * (-1)

            if minimum >= 0:
                if diff < minimum:
                    minimum = diff
                    loc = i
              #  print(loc)

            else :
                minimum = diff
                loc = i
             #print(loc)
        if(s.isdigit()):     
            magic_char = chr(53)
        elif(s.isupper()):     
            magic_char = ALPHA[loc-65]
        else :
            magic_char = ALPHA[loc-71]
        magic_word += str(magic_char)

    print (magic_word)
