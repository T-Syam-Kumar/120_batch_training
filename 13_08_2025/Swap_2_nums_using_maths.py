def swap(num1,num2):
    print(f"before swaping a : {num1}  b : {num2}")
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    print(f"after swaping  a : {num1} b : {num2}")
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
swap(a,b)