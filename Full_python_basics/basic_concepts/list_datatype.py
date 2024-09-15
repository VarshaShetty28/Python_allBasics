# List Datatype in python
from logging import getLevelName

products = ['pen','pencil','sketches']
print(type(products))
price=[5,5,50]
print(products,price)
isAvailable=[True,False]
mixed=[5,'pen',60,90.856,True,['Virat','Singer','Male',21]]
print(isAvailable,mixed)
print(len(mixed))
print(mixed[-1])
print(mixed[-1][0])
#another way to represent list
names=list(('varsha','varshini'))
print(names)
names[0]='HYE'
print(names)
print(mixed)
mixed[2:4]=["Hello","Namaskara"]
mixed.pop(4)#To pop
mixed.insert(2,"PENCIL")#for insert
print(mixed)







