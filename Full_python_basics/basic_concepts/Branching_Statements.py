#####   LOOPS #####
## WHILE LOOP AND FOR LOOP are the only two loops in python(To implement Do ehile loop in python we use WHILE AND ELSE)
i=0
while(i<10):
    print(f"{i+1})Hello World")
    i+=1

#####  FOR LOOP ########

#for i in range(10):
 #   print(f"This is {i+1}")

mixed=[5,'pen',60,90.856,True,['Virat','Singer','Male',21]]
for i in mixed:
     print(mixed) # It is going to print on the basis of the number of items in the list here it is 6 so it takes i as 6 , it excutes 6 times
for i in mixed:# i can be replaced anything
     print(i)#To print the elements only

###########################################################################################
##########################################################################################
##########  Printing L pattern in For loop  ###############################

list=[2, 2, 2, 2, 5, 5]
for i in list: # i can be replaced anything
    print("* "*i)

############################
for num in range(31):
    if num%3==0:
        print(num)


###############################################################################################
################################## DO WHILE loop representation in python ####################################
i=100
while(i<10):
    print(i)
else:
    print("Not less than 10")
###########################################################
for i in range(100):
    if i % 3 == 0:      # Check if i is divisible by 3
        if i == 30:     # Stop the loop when i equals 30
            continue
        print(i)
