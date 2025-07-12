##################   functions     ##################
# Functions are the block of code that can be used for our future use instead of writing entire code can just call the function
def table(num):
    for i in range(11):
        print(num*i)
def repeat(num):
    for i in range(num):
        print(f"This line made me to repeat {num} times")


print("1. Table\n2. Repeat")
Option=int(input('Option>>  '))


if Option==1:
    num=int(input("Enter the number for which you want table: "))
    table(num)
elif Option==2:
    num=int(input("Enter the number for which you want repeat: "))
    repeat(num)
else:
    print("Invalid Option")
