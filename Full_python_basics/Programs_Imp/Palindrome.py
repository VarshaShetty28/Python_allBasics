# Plaindrome is a string which can be read same in front and back as same 
# eg : MOM , Malayalam ,abba etc 
# input string ----- out put bool val (True , False)
# since we are using 2 pointers in  left and rigt using while loop is easier 
def PalindromeCheck(str):
    leftIdx = 0
    RightIdx = len(str)-1 # since puython starts with 0 idx
    res = True
    while(leftIdx < RightIdx):
        if str[leftIdx].lower() != str[RightIdx].lower():
            res = False
            break
        leftIdx+=1
        RightIdx-=1
    print(res)
PalindromeCheck("Malayalam")
PalindromeCheck("hello")