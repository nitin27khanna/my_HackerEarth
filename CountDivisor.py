#left range: l
#right range : r
#divisor : k

l,r,k =  input().split(' ')


#print (l,r,k)

count = 0
for i in range (int(l),(int(r)+1)):
    if i%int(k) == 0:
        count = count +1
    
print(count)
