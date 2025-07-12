# function to search in a sorted integer array 
# if it is sorted we can make it optimized and fast 
# problem is : search a integer in sorted array :
# this is the binary search algorith which works only for the sorted array 
def search(num,key):
    left = 0
    right = len(num)-1
   
    found = 0 
    while(left <= right):
        mid = int((left+right)/2)
        if num[mid] == key:
            found = 1
            break #breaking is very imp inside any loop or else it will be keep running
        elif num[mid] > key :
            right = mid-1
        elif num[mid] < key:
            left = mid+1
    if found == 1:
        print(f'Number is found and the location of the number is (index is) : {mid}')
    else:
        print('Number is not found')

num = [1, 2, 3, 5, 7, 8, 9, 10, 15, 45]
key = 11
search(num,key)