##number of testcases
tests = int(input())

for i in range (0,tests):
    length = int(input())
    string = input()
    num = []
    count = ""
    for s in string:
        if s.isdigit():
            #make a string of digits
                count += str(s)
                
              #  print (count)
        else:
            if count != "":
                #append complete count to num
                num.append(count)
                count = ""
  
  ## if string is xxxxxxxxxxx[a-z]4 then to cover 4 we need this segment
    if count != "":
        
        num.append(count)
    
    print(len((num)))

            
