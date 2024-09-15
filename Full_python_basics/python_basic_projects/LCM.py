print("\n**********Lets find the LCM of two number************* \n")

num1 = int(input("num1>> "))
num2 = int(input("num2>> "))

if num1>num2:
    Greater=num1
else:
    Greater=num2

while(True):
    if Greater%num1==0 and Greater%num2==0:
        LCM=Greater
        break
    Greater+=1
print(f"The LCM of {num1} and {num2} is {LCM}")

