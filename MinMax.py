##check if all the numbers exist between min and max in array

##single iteration of selection sort
def get_max(arr):
    maxi = int(arr[0])
    for i in arr:
        if int(i) > maxi:
            maxi = int(i)
    return maxi

##single iteration of selection sort
def get_min(arr):
    mini = int(arr[0])
    for i in arr:
        if int(i) < mini:
            mini = int(i)
    
    return mini
    
    
length = int(input())

arr = input().split(' ')

maxi = get_max(arr)
mini = get_min(arr)


for i in range (0 , length):
    arr[i] = int(arr[i])

check_arr = [w for w in range (mini,maxi+1)]
#print(check_arr)
msg = "YES"
for i in check_arr:
    if int(i) not in arr:
        msg = "NO"

print(msg)
