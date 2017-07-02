#number of testcases
tests =  int (input())

#looping the number of iterations of the prog

for i in range(0,tests):
    Week = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
    
    #input number of topics
    topics = int(input())
    index = 0
    #make an array of days
    arr=[]
    arr = input().split()
    tot_counted = 0
    #take inputs for days and topics
    i=0
    while tot_counted < topics:
        tot_counted += int(arr[i])
        if tot_counted >= topics:
            index = i
            #print (index)
            break
        else :
            i = (i+1)%7 
            
    print(Week[(index)])
        
    
    
