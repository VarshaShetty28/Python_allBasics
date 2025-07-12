#Tupple data types
#Tupples is similoar to list but the thing is we cant change the values in tupples but in list we can modify it using indexes
from math import trunc

my_passwords = (1325,5236,7458,8569)
print(my_passwords)
#my_passwords[0]=1236    #Here this is not valid in TUPPLE but we can modify like this in list so it shows the TypeError tuple
print(my_passwords)

#Other way of assigning tupple is
my_passwords2 = tuple((1325,5236,7458,8569))
mixed_tupples = (1325, "varsha", True, 8.526, [1, 2, 3, 4], tuple((5, 4, 8)))
print(mixed_tupples)
print(type(my_passwords2))
print(type(my_passwords))
print(mixed_tupples[0]) #To acces the elements in the tupple
#######################################################################################################
########################      SETS      ###############################################
#SETS means the collection of objects

my_sets={1,2,3,4,5,5}
#print(my_sets[0])  # This is not valid for sets becuase TypeError: 'set' object is not subscriptable
print(my_sets)

#######################################################################################################
########################      DICTIONARY(KEY VALUE pairs)      ###############################################

Oxford_dict={"Names":100,"ages":20-35,"gender":"M/F"}
print(Oxford_dict["gender"])

Oxford_dict1={"Names":100,
              "ages":20-35,"gender":"M/F",
              "likes":1000,"subscribers":10000}
print(Oxford_dict1["subscribers"])
print(f"Oxford dictionary has {Oxford_dict1['subscribers']} subscribers and {Oxford_dict1['likes']} likes")

Oxford_dict2={"Names":100,
              "ages":'20-35',"gender":"M/F",
              "likes":1000,"subscribers":10000}
print(Oxford_dict2["subscribers"])
Oxford_dict2["subscribers"]=11000 #To change the value in the dictionary
print(Oxford_dict2["subscribers"])
#Only to see the keys of the dictionary is
print(Oxford_dict2.keys())
#Only to see the Values of the dictionary is
print(Oxford_dict2.values())
#TO POP or UPDATE the values in a dictionary
Oxford_dict2.pop("likes")
print(Oxford_dict2)
#pop items to pop the last item
Oxford_dict2.popitem()
Oxford_dict2.update({"comments": 2000}) #To update the new key and value to the dictionary 
print(Oxford_dict2)