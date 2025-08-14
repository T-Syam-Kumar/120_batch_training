def even_n_1(n):
    if n == 0:
        return
    print(n,end=" ")
    even_n_1(n-2)
even_n_1(10)
print()
def even_1_n(n):
    if n > 10:
        return
    print(n,end=" ")
    even_1_n(n+2)
n = 2
even_1_n(2)
print()
def odd_1_n(n):
    if n<0:
        return
    print(n,end=" ")
    odd_1_n(n-2)
n = 25
odd_1_n(n-1 if n%2 == 0 else n)
print()
