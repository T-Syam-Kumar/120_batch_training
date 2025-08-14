def clear_first_bit(value,index):
    temp = 1<<index
    temp-=1
    ans = value & temp
    print(ans)
n = int(input("enter the value : "))
m = int(input("enter the index : "))
clear_first_bit(n,m)