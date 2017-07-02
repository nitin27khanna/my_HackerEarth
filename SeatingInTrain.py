#window seats 3i and 3i+1

def get_seat(opp,i):
    
    if opp == 0:
        opp_seat_no = 12 * ((i//12)+1)
    
    elif opp == 1:
        opp_seat_no = 12 * ((i//12)-1) + 1
    
    else :
        opp_seat_no = 12 * ((i//12)) + opp
    
    return (opp_seat_no)
        
        
        
dic_seats=  {1:'WS',2:'MS',3:'AS',4:'AS',5:'MS',6:'WS',7:'WS',8:'MS',9:'AS',10:'AS',11:'MS',0:'WS'}

#enter number of testcases
T = int(input())
testcases = []
#enter testcases
for i in range(0,T):
    t = int(input())
    testcases.append(t)

for i in testcases:
    rem = i % 12
    if rem == 1:
        opp = 0
    elif rem == 2:
        opp = 11
    elif rem == 3:
        opp = 10
    elif rem == 4:
        opp = 9
    elif rem == 5:
        opp = 8
    elif rem == 6:
        opp = 7
    ###########    
    elif rem == 7:
        opp = 6
    elif rem == 8:
        opp = 5
    elif rem == 9:
        opp = 4
    elif rem ==10 :
        opp = 3
    elif rem == 11:
        opp = 2
    elif rem == 0:
        opp = 1
    
    opp_seat = get_seat(opp,i)
    print (opp_seat,dic_seats[opp])

