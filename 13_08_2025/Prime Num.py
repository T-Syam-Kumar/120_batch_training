n = int(input("Enter a number : "))
flag = 0
if n < 0 or n == 0 or n == 1:
    print("enter a number greater than 1")
elif n == 2 or n == 3:
    print("Prime Number")
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print("not a prime number")
else:
    i = 5
    while (i * i <= n) : 
        if n % i == 0 or n % (i + 2) == 0: 
            flag = 1 
        i += 6
    print("prime number" if flag == 0 else "not a prime number")
    """
    for i in range(5,int(n**0.5)+1):
        if n % i == 0:
            flag = 1
            break
    print("prime number" if flag == 0 else "not a prime number")"""

#another logic for else block
