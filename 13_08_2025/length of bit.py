def count_bits(value):
    count = 0
    while value > 0 :
        value = value>>1
        count+=1
    print(count)
value = int(input("enter a number : "))
count_bits(value)
