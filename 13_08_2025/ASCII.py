s = "Mango"
sum = 0
for i in s:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        sum+=ord(i)-64
    else:
        sum+=ord(i)-96
print(sum)