
# In Python, a: int or a:int are just a type hint—it helps developers and tools understand expected types but doesn't enforce them at runtime 
def addNumber(a:int,b) ->int:
    return a+b
a = int(input("Enter the 1st number : "))
b = int(input("Enter the 2nd number : "))
total = addNumber(a,b)
print(total)
