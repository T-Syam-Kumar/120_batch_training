n = input("enter a string : ")
m = int(input("enter the no of rotation : "))
x = len(n)
z = m%x
print("Right Rotation : ",n[-z:]+n[:-z])
print("left Rotation : ",n[z:]+n[:z])