# reverse the given string 
# input -> pgm -> output without using the another varibla 
# in the same varble need to reverse 
# Reversing the sring in original string which is called in-place or in-memory 
# But in python the strings ar immutable we cant chage the string 
# so we need to add the reversed string to the new location 
# the unsued varibles will get freed by garbage collection
# In python zip is used to call multiple rage finction so we can ryt two for loop in on eline using zip
#  
def rverseString(str):
    n = len(str)
    mid = int(n/2)
    # for i,j in zip((0,mid-1),(n-1,mid+1)):
    #     str[i],str[j] = str[j],str[i] this will throwerror in python bcs strings are immutable in python cant change string in the same variables
    new_str = []
    for j in range(n-1,-1,-1): # in python while reversing we need to specify the step bcs it usaully increse the step so 
        new_str.append(str[j])
    print(''.join(new_str)) #''.join is used to conver the string to normal string 

words = "abcd"
rverseString(words)