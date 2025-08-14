def rec_nto1(n):
    if n == 0:
        return
    print(n,end=" ")
    rec_nto1(n-1)
rec_nto1(10)
print()
def rec_1ton(m):
    if m == 11:
        return
    print(m,end=" ")
    rec_1ton(m+1)
rec_1ton(1)
print()

def rec_1_n(n):
    if n != 0:
        rec_1_n(n-1)
        print(n,end=" ")
rec_1_n(15)
print()
def rec_n_1(n):
    if n != 0:
        print(n,end=" ")
        rec_n_1(n-1)
rec_n_1(15)