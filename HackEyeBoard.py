n = int(input())

x,y,p = input().split(" ")

x = int(x)
y = int(y)
p = int(p)


for i in range (0,n):
    
    for j in range (0,n):
        if(i==x and j==y):
            print (p,end=" ")
            
        else:
            d1 = (i - x) if x < i else (x - i) 
            d2 = (j - x) if x < j else (x - j) 
            to_print =  (p - d1) if d1 > d2 else (p - d2) 
            to_print = 0 if to_print < 0 else to_print 
            print(to_print,end=" ")
    print('')    
    

