a = int(input("Enter a num : "))
sum = 0
while a > 9:
    a = str(a);sum = 0
    for i in a:
        sum += int(i)
        a = sum
print(sum)











"""i = 0
while(n >= 1):
    for a in s:
        sum = sum + int(s[i])
        i = i+1
    s = sum
print(sum)"""
