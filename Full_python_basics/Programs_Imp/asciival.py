#fibd the length of the string 
#in string we need to handle all te cases like non and all
#to find the ascii value in python we need to use the ord function to that char can be used to find teh value of digit also
def getStringlength(str):
    print(len(str))
def StringLengthcount(str):
    count = 0
    if str != None:
        for i in str:
            count+=1
        print(count)
    else:
        print('none canot be iteratable')
    

def printAsciValv(str):
    for char in str:
        print(ord(char))
printAsciValv('1')
getStringlength('stringssss')
StringLengthcount('None')
StringLengthcount(None)