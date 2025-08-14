#we should add 1 to taken single number 
a = [9]
sum = ""
for i in a:
    sum = sum + str(i)
sum = str(int(sum) + 1)
#print(sum)
l = []
for i in sum:
    l.append(int(i))
print(l)
