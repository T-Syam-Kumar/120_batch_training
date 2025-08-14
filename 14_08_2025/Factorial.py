def fact(n):
    sum = 0
    if n == 1:
        return 1
    return n*fact(n-1)
print(f"ans is {fact(int(input("Enter a number : ")))}")