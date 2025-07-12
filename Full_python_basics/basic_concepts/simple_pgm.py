def motivator(name):
    print(f"Hey {name}, you're strong! Don't worry!")

def addname():
    return input("Enter your name: ")

msg = input("Enter your sad moment: ")
name = addname()

if name and msg:
    motivator(name)

elif not name and msg:
    for i in range(5):
        print("Please enter your name.")
        name = addname()
        if name:
            motivator(name)
            break
    else:
        print("Sorry! We gave you 5 chances to enter your name but you did not, so exiting the program.")

elif name and not msg:
    print("Hey, happy to hear that you don't have any problems!")

else:
    print("Ohhh sorry, you haven't entered anything.")
