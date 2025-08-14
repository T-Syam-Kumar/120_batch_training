# Concat 2 strings and upper case
a = "abc"
b = "abcd"
res = ""
i = 0
while i<len(a) and i<len(b):
    res += a[i] + b[i]
    i+=1
res += a[i:].upper()
res += b[i:].upper()
print(res)