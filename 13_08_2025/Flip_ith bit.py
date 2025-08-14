def flip_ith_bit(value,index):
    temp = 1<<index
    res = value^temp
    print(res)
m = int(input("enter the value : "))
n = int(input("Enter the index : "))
flip_ith_bit(m,n)