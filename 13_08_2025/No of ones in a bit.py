def count_no_of_ones(value):
    count = 0
    while value>0:
        count+=(value&1)
        value = value>>1 #value>>=1
    print(count)
n = int(input("enter a number : "))
count_no_of_ones(n)