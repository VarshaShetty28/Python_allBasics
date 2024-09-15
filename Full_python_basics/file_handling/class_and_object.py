# Classes and objects 
# Object Oriented Programming = it is written on the basis of classes which are interrelated and inside the class the object is defined which is the instance of the class

class Team: # Class name
    # pass : if class is empty just pass this variable 
    name = ""
    capt = ""
    ban = ""

    def winRcbFansReview(self):    # this is method the function inside the class is called Method
        if self.name=="RCB" :
            return("E sala cup Namdee !!!!!")
        elif self.name=="CSK":
            return("Eradu sala navu BAN agilla............... ha ha ")  # Nothing will happen if you put print insted of return but in the output will get one none value 
# so inside the class use return instead of print 

T1 =Team()     # T1 is the object
T1.name="RCB"
T1.capt="VK"

T2=Team()      # T2 is the object
T2.name="CSK"
T2.capt="MSD"

print("If RCB won the match , Then RCB fans Will be >>........")
print(T1.winRcbFansReview())
print("If RCB loss the match , Then RCB fans Will be >>........")
print(T2.winRcbFansReview())