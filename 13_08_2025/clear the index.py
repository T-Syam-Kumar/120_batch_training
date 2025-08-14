def clear_ithbit(value,index):
    temp = 1<<index
    temp = ~temp
    value = value & temp 
    print(value)
n = int(input("enetr a value : "))
m = int(input("enter the index : "))
clear_ithbit(n,m)