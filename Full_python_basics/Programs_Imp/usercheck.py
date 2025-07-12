# if 0 is writen inside '' is inside single quote it will take teh asci value '0'asci val of 0
# in python we have a vuiltin isdigit() we can use that as well 
def isDigit(val):
    flag = True
    for i in range(len(val)):
        if val[i] < '0' or val[i]  > '9':
            print(f"The non digit character found at {i} and the non digit character is {val[i]}")
            flag = False
    if flag:
        print("It is all digit")
    else:
        print("It is all not digit")

value = input("Enter anything ....\n")
print(f"Using the builtin the given value is digit {value.isdigit()}")
isDigit(value)



# Hardware → OS → Drivers(keyboard,mouse) → APIs/Libraries → Program (e.g., scanf uses system calls to access input via drivers using the librarys present above the os)

