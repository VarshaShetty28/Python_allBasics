#in python we can use the just swap keyword to swap two numbers 
def swapsimple(num1,num2):
    return num2,num1 #returning two vars is available in python
def swaping(num1,num2):
    print(f'before swaping values are num1 is {num1} and num2 is {num2}')
    temp = num1
    num1=num2
    num2=temp
    print(f'Swaped values are num1 is {num1} and num2 is {num2}')

num1 = 5
num2 = 10
print(f'before swaping values are num1 is {num1} and num2 is {num2}')
# swaping(num1,num2)
nums1 , nums2 = swapsimple(num1,num2)
print(f'Swaped values are num1 is {nums1} and num2 is {nums2}')