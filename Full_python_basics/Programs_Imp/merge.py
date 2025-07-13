# need to merge the two arrays given in to a single array 
def MergeArray(num1,num2):
    num1 = num1 +num2
    return num1
def mergeAppend(num1,num2):
    for i in num2:
        num1.append(i)
    return num1
   

num1 = [1,2,3]
num2 = [4,2,3]
final_res = MergeArray(num1,num2)
print(final_res)
final_otpt = ' '.join(str(x) for x in final_res)
print(final_otpt)

A_ans = mergeAppend(num1,num2)
print(A_ans)