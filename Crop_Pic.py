##limit to check
limit = int(input())
## number of inputs 
noi = int(input())

lst = []

for i in range(0,noi):
    a,b = (input().split(" "))
  #  print(a,b)
    lst.append(int(a))
    lst.append(int(b))
i = 0
while i <len(lst):
    if (lst[i] < limit) or (lst[i+1] < limit):
        print("UPLOAD ANOTHER")
    else:
        if lst[i] == lst[i+1]:
            print("ACCEPTED")
        else:
            print("CROP IT")
   
    i = i + 2        
