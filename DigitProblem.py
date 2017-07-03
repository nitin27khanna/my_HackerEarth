##enter the X and K

X,K = input().split(" ")
K = int(K)

#print (X,K)
lst = []
for each in X:
    lst.append(int(each))
k=K
#print (lst)
ans=[]
for x in lst:

    if k == 0 or x == 9:
        ans.append(x)
    
    elif x != 9 and k > 0:
        ans.append(9)
        k=k-1
        

number = 0
for i in ans:
    number = number * 10 + i
    
print (number)
