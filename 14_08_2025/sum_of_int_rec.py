def sum_int(n):
    if n<10:
        return n
    return n%10 + sum_int(n//10)
print(sum_int(544))

# count the digits 
def count_int(n):
    if n<10:
        return 1
    return 1 + count_int(n//10)
print(count_int(544))