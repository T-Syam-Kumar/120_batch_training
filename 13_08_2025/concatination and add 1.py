"""#we should add 1 to taken single number 
a = [9]
sum = ""
for i in a:
    sum = sum + str(i)
sum = str(int(sum) + 1)
#print(sum)
l = []
for i in sum:
    l.append(int(i))
print(l)"""

a = [9,9,9,9,9]
for i in range(len(a)-1,-1,-1):
    if a[i]+1 == 10:
        a[i] = 0
    else:
        a[i]+=1
        break
else:
    a = [1] + a
print(a)