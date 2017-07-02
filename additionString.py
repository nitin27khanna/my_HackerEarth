
#string to check offset
string = "abcdefghijklmnopqrstuvwxyz"

#enter the number of tests

tests = int(input())

for i in range(0,tests):
    inp = list(input())
    string_ans = ""
    ##print (inp)
    s = 0
    while s < len(inp)   :
        offset   = string.index(inp[s])
        offset_r = string.index(inp[(len(inp)-s-1)])
        string_ans += str(string[(offset+offset_r+1)%26])
        s = s+1
        
    print (string_ans)
