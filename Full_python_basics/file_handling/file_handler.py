#create a object and open the required file 
########### NOTE : Please comment the other opearions while performing one opearion here bcs everything is written in a single file 

#Read operation
g=open("demo_file.txt","rt")
print(g.read()) #read the file which is opened 
print(g.readline()) # To read the single line of the file mainlt the first line and if you excute this second time it exwcutes the 2nd line 

# write operation
g=open("demo_file.txt","wt")
g.write("Hello am varsha") # This is to write to the existing file so that the old contents are overwritten by the new write statement 

# Append opeartion
g=open("demo_file.txt","a")
g.write("Hello am varsha") # This is to write to the existing file so that the old contents are overwritten by the new write statement 

# create and write 
g=open("demo.txt","x")
g.write("Hello am varsha") # This is to write to the existing file so that the old contents are overwritten by the new write statement 

g.close()


# r = read 
# w = write to existing file
# a = append
# x = create file and write

# t = text
# b = binary
# change the parameter  as needed like ( rt,wt,wb,rb)


# To delete the created files import one library 

import os

os.mkdir("Varsha") # To make the directory named varsha 
os.rmdir("Varsha") # To remove the directory 

# To remove the file use remove command 
os.remove("demo_file.txt")