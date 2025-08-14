a = [1,2,3,4,5,6,5]
flag = 0
for i in range(1,len(a)-1):
    if a[i+1] != 1 + a[i]:
        flag = 1
        break
print("Sorted" if flag == 0 else "not sorted")

