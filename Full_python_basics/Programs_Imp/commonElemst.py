# write common elemnets prenst in two array its is used in ap0plivations oike insrta
# in instal who are teh common frond among two can buit from this logic

def commonElements(num1,num2):
    common = []
    for n1 in num1:
        for n2 in num2:
            if n1==n2 and n1 not in common:
                common.append(n1)
            else:
                continue
    print(common)

num1 =[1,2,3,6,5,9,4,3,9]
num2 = [1,6,5,9,6,2,9,2,6]
commonElements(num1,num2)