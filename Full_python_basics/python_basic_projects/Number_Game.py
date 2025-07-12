import random
secret_num=random.randint(1,50)
counter=1
while(True):
    guess=int(input('\nGuess the number btw 1-50: '))
    if guess==secret_num:
        print("***********Awsome!!! You Guesse it !! Victoryyyy*****************")
        break 
    else:
        counter+=1
        if guess<secret_num:
            print("Aww!!! Please Guess Higher Number ")
        elif guess>secret_num:
            print("Aww!!! Please Guess lower Number ")
print(f"The number of attempts : {counter}\n")
