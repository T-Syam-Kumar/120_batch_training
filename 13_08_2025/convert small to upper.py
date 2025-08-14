s = "aBCdeF"
l = []
for i in s:
    if ord(i) in  range(97,123):
        x = chr(ord(i)-32)
        l.append(x)
    else:
        x = chr(ord(i)+32)
        l.append(x)
print("".join(l))
