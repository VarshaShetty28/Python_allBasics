print("\n***********  Simple Calculator  *************\n")
print("Select an operation\n")
print("1. Multiplication")
print("2. Addition")
print("3. Subtration")
print("4. Division")
print("5. Modulus")
print("6. Exit\n")

while True:
    operation= int(input("Operation>> "))
    
    if operation == 6:
        print("Exiting the calculator. Goodbye!\n")
        break
    if operation < 1 or operation > 6:
        print("Invalid option! Please try again.........\n")
        continue
    
    print("Enter num1 and num2 : ")
    num1=float(input("num1>> "))
    num2=float(input("num2>> "))

    if operation==1:
        print("Multiplication: ",num1*num2)
    elif operation==2:
        print("Addition: ",num1+num2)
    elif operation==3:
        print("Subtration: ",num1-num2)
    elif operation==4:
        if num2 != 0:
            print("Division: ", num1 / num2)
        else:
            print("Error: Division by zero is not allowed!")
    elif operation==5:
        print("Modulus: ",num1%num2)
    else:
        print("Some error are there please try again !!!!!!")
print("\n------------------------------\n")

