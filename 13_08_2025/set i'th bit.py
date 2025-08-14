def extract_bit(value,index):
    temp = 1<<index
    res = value | temp
    print(res)
    #print(value | (1<<index))

n= int(input("Enter a value : "))
m = int(input("enter the index : "))
extract_bit(n,m)