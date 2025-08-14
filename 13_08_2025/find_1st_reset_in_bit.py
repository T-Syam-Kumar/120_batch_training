def find_1st_set_bit(value):
    count = 0 
    while (value & 1 == 1):
        value = value>>1
        count+=1
    print(count)
n = int(input("Enter a number : "))
find_1st_set_bit(n)