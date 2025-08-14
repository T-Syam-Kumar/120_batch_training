#arr = list(map(int,input.split()))
arr = [1,2,3,4,5]
i = 0
j = 1
while(j<len(arr)):
    if arr[i]%2 == 0 and arr[j]%2 != 0:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j+=1
    elif arr[i]%2!= 0 and arr[j]%2 == 0:
        i+=1
        j+=1
    else:
        j+=1
print(arr)
