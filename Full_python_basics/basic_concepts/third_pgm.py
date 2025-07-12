# def myfunction():
#     print("Hyeeeeeeeeeee")
# myfunction()

# def my_function(fname,sname):
#     print(fname +" " + sname + " "+ "something")
# my_function("Email","hello")    

def new_function(*args): #its not a pointer 
    print(*args)
    print(args)
new_function("first","second","Third")