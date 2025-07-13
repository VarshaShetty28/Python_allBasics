# find and print unique elements in a array 
# we can add se functin wil get the uniwue values
# but we need not able to use this in some pgms
# i/p: 1 4 1 8 9 4 -? pgm -> o/p : 1 4 8 9 
# cand do bu comparin ge ach char or we can fing whether the val is asded prvlsy


def uniqueElements(nums):
    for i in range(0,len(nums),1):
        isUnique = False
        for j in range(i+1,len(nums),1):
            if nums[i] == nums[j]:
                isUnique = True
                break
        if isUnique == False:
            print(nums[i])

def uniqueElements2(nums):
    result = []
    for i in nums:
        if i not in result:
            result.append(i)
    for num in result:
        print(num, end=' ')

inputs = [1, 2, 6, 6, 6, 9, 3]
uniqueElements(inputs)


inputs = [1, 2 ,6 ,6,6,9,3]
uniqueElements(inputs)