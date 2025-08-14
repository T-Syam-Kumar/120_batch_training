n = int(input())
s= 0
for i in str(n):
    if i in "2357":
        s+=int(i)
print(s)