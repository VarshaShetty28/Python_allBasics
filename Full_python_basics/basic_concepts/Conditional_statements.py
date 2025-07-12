print("Enter the tree values for A,B and C(Enter integer values only):")
a=int(input("A>>\t"))
b=int(input("B>>\t"))
c=int(input("C>>\t"))

if a>b and a>c:
    print("A is Greater ")
elif b>a and b>c:
    print("B is Greater")
elif (a == b == c) or (a==b) or (b==c) or (a==c):
    print("All are equal/ Any two numbers are equal")
else:
    print(("C is Greater"))